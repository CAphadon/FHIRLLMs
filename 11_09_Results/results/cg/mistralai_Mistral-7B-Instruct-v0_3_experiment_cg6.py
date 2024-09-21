import xml.etree.ElementTree as ET
import json

def convert_to_fhir(xml_file):
    # parse xml file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # initialize FHIR bundle
    bundle = {"resourceType": "Bundle", "type": "transaction", "entry": []}

    # iterate through ADT_GEKID nodes
    for adt_gekid in root.findall('ns0:ADT_GEKID'):
        # create Patient resource
        patient_resource = {"resourceType": "Patient", "id": "", "meta": {"source": "", "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]}, "identifier": [], "gender": "", "birthDate": "", "address": []}

        # iterate through Absender nodes
        for absender in adt_gekid.findall('ns0:Absender'):
            # add Absender information to Patient resource
            patient_resource["identifier"].append({"type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "PSEUDED"}, {"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical\u00b7record\u00b7number"}]}, "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id", "value": absender.find('ns0:Absender_ID').text})
            patient_resource["gender"] = absender.find('ns0:Absender_Geschlecht').text
            patient_resource["birthDate"] = absender.find('ns0:Absender_Geburtsdatum').text
            patient_address = []
            absender_anschrift = absender.find('ns0:Absender_Anschrift')
            if absender_anschrift is not None:
                patient_address.append({"type": "both", "postalCode": absender_anschrift.text.split(',')[0], "country": "DE"})
            patient_resource["address"] = patient_address

        # iterate through Menge_Patient nodes
        for menge_patient in adt_gekid.findall('ns0:Menge_Patient'):
            # iterate through Patient nodes
            for patient in menge_patient.findall('ns0:Patient'):
                # create Patient_Stammdaten resource
                patient_stammdaten_resource = {"resourceType": "Patient", "id": "", "identifier": [], "name": [], "gender": "", "birthDate": "", "address": []}
                # iterate through KrankenversichertenNr, KrankenkassenNr, Patienten_Nachname, Patienten_Vornamen, Patienten_Geschlecht, Patienten_Geburtsdatum nodes
                patient_stammdaten_resource["identifier"].append({"system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id", "value": patient.find('ns0:KrankenversichertenNr').text})
                patient_stammdaten_resource["name"].append({"given": [patient.find('ns0:Patienten_Vornamen').text], "family": patient.find('ns0:Patienten_Nachname').text})
                patient_stammdaten_resource["gender"] = patient.find('ns0:Patienten_Geschlecht').text
                patient_stammdaten_resource["birthDate"] = patient.find('ns0:Patienten_Geburtsdatum').text
                patient_address = []
                patient_anschrift = patient.find('ns0:Menge_Adresse')
                if patient_anschrift is not None:
                    for adresse in patient_anschrift.findall('ns0:Adresse'):
                        patient_address.append({"type": "both", "postalCode": adresse.find('ns0:Patienten_PLZ').text, "country": "DE"})
                patient_stammdaten_resource["address"] = patient_address

                # iterate through Menge_Meldung nodes
                for menge_meldung in patient.findall('ns0:Menge_Meldung'):
                    # create Meldung resource
                    meldung_resource = {"resourceType": "Observation", "id": "", "subject": {"reference": f"Patient/{patient_stammdaten_resource['id']}"}, "status": "final", "code": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "ADT"}]}, "valueCodeableConcept": {"text": "ADT"}}
                    # iterate through Meldung_ID, Melder_ID, Meldedatum, Meldebegruendung, Meldeanlass nodes
                    meldung_resource["id"] = menge_meldung.find('ns0:Meldung_ID').text
                    meldung_resource["valueDateTime"] = menge_meldung.find('ns0:Meldebegruendung').text
                    meldung_resource["valueCodeableConcept"] = {"text": menge_meldung.find('ns0:Meldeanlass').text}

                    # iterate through Tumorzuordnung nodes
                    for tumorzuordnung in menge_meldung.findall('ns0:Tumorzuordnung'):
                        # create Diagnosis resource
                        diagnosis_resource = {"resourceType": "Diagnosis", "id": "", "subject": {"reference": f"Patient/{patient_stammdaten_resource['id']}"}, "code": {"coding": [{"system": "https://fhir.diz.uk-erlangen.de/terminology/icd-10", "code": tumorzuordnung.find('ns0:Primaertumor_ICD_Code').text}]}}
                        # iterate through Tumor_ID, Diagnosedatum, Seitenlokalisation nodes
                        diagnosis_resource["id"] = tumorzuordnung.find('ns0:Tumor_ID').text
                        diagnosis_resource["dateDiagnosed"] = tumorzuordung.find('ns0:Diagnosedatum').text
                        diagnosis_resource["site"] = tumorzuordnung.find('ns0:Seitenlokalisation').text

                        # add Diagnosis resource to Meldung resource
                        meldung_resource["composition"].append({"item": [diagnosis_resource]})

                    # iterate through Menge_ST nodes
                    for menge_st in menge_meldung.findall('ns0:Menge_ST'):
                        # create Treatment resource
                        treatment_resource = {"resourceType": "Procedure", "id": "", "status": "completed", "subject": {"reference": f"Patient/{patient_stammdaten_resource['id']}"}, "code": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/sNOMEDCT", "code": menge_st.find('ns0:ST_Stellung_OP').text}]}}
                        # iterate through ST_ID, ST_Intention, ST_Zielgebiet, ST_Seite_Zielgebiet, ST_Ende_Datum, ST_Ende_Grund, Menge_Nebenwirkung nodes
                        treatment_resource["id"] = menge_st.find('ns0:ST_ID').text
                        treatment_resource["statusReason"] = menge_st.find('ns0:ST_Ende_Grund').text
                        treatment_resource["code"].append({"coding": [{"system": "http://terminology.hl7.org/CodeSystem/sNOMEDCT", "code": menge_st.find('ns0:ST_Stellung_OP').text}]})
                        treatment_resource["procedureCode"].append({"coding": [{"system": "http://terminology.hl7.org/CodeSystem/sNOMEDCT", "code": menge_st.find('ns0:ST_Zielgebiet').text}]})
                        treatment_site = []
                        if len(menge_st.findall('ns0:ST_Zielgebiet')) > 1:
                            for st_zielgebiet in menge_st.findall('ns0:ST_Zielgebiet'):
                                st_site = {"location": {"description": st_zielgebiet.text}}
                                if st_zielgebiet.text.startswith("5."):
                                    st_site["type"] = "bodySite"
                                elif st_zielgebiet.text in ["1.2", "1.3", "1.4", "1.5"]:
                                    st_site["type"] = "anatomicSite"
                                else:
                                    st_site["type"] = "organSystem"
                                st_site["value"] = st_zielgebiet.text.replace("T", "R").replace("R", "L")
                                treatment_site.append(st_site)
                        else:
                            treatment_site.append({"location": {"description": menge_st.find('ns0:ST_Zielgebiet').text}})
                        treatment_site_reference = {"reference": f"StructureDefinition/BodySite{treatment_site[0]['type']}"} if len(treatment_site) > 1 else {"reference": f"StructureDefinition/BodySite"}
                        treatment_resource["location"}.update(treatment_site_reference)
                        treatment_site_value = treatment_site[0]["value"] if len(treatment_site) > 1 else treatment_site[0]["location"]["description"]
                        treatment_resource["location"].update({"value": treatment_site_value})

                        # iterate through Menge_Bestrahlung nodes
                        for menge_bestrahlung in menge_st.findall('ns0:Menge_Bestrahlung'):
                            # create RadiationTherapyTreatmentSite resource
                            radiation_therapy_treatment_site_resource = {"resourceType": "RadiationTherapyTreatmentSite", "id": "", "status": "completed", "subject": {"reference": f"Patient/{patient_stammdaten_resource['id']}"}}
                            # iterate through Bestrahlung nodes
                            for bestrahlung in menge_bestrahlung.findall('ns0:Bestrahlung'):
                                # create RadiationTherapyTreatment resource
                                radiation_therapy_treatment_resource = {"resourceType": "RadiationTherapyTreatment", "id": "", "subject": {"reference": f"Patient/{patient_stammdaten_resource['id']}"}}
                                # iterate through ST_Zielgebiet, ST_Seite_Zielgebiet nodes
                                radiation_therapy_treatment_resource["statusReason"] = bestrahlung.find('ns0:ST_Ende_Grund').text
                                radiation_therapy_treatment_resource["doseDeliveredQuantity"].append({"value": bestrahlung.find('ns0:Bestrahlung_Dosis').text, "unit": "Gy"})
                                radiation_therapy_treatment_site_resource["radiationOncologyTreatment"].append({"reference": f"RadiationTherapyTreatment/{radiation_therapy_treatment_resource['id']}"})
                                radiation_therapy_treatment_site_resource["site"] = {"description": bestrahlung.find('ns0:ST_Zielgebiet').text}
                                if bestrahlung.find('ns0:ST_Zielgebiet').text.startswith("5."):
                                    radiation_therapy_treatment_site_resource["site"}.update({"type": "bodySite"})
                                elif bestrahlung.find('ns0:ST_Zielgebiet').text in ["1.2", "1.3", "1.4", "1.5"]:
                                    radiation_therapy_treatment_site_resource["site"}.update({"type": "anatomicSite"})
                                else:
                                    radiation_therapy_treatment_site_resource["site"}.update({"type": "organSystem"})
                                radiation_therapy_treatment_site_resource["site"}.update({"value": radiation_therapy_treatment_site_resource["site"]["description"].replace("T", "R").replace("R", "L")})

                                # add RadiationTherapyTreatmentSite resource to RadiationTherapyTreatment resource
                                radiation_therapy_treatment.append(radiation_therapy_treatment_site_resource)

                            # add RadiationTherapyTreatment resource to Treatment resource
                            treatment_resource["procedure"].append(radiation_therapy_treatment)

                        # add Treatment resource to Meldung resource
                        meldung_resource["procedure"].append(treatment_resource)

                    # add Meldung resource to patient_stammdaten_resource
                    patient_stammdaten_resource["composition"].append({"item": [meldung_resource]})

                # add patient_stammdaten_resource to patient_resource
                patient_resource["resource"].append(patient_stammdaten_resource)

        # add patient_resource to bundle
        bundle["entry"].append({"fullUrl": f"Patient/{patient_resource['id']}", "resource": patient_resource})

    # print FHIR json
    print(json.dumps(bundle, indent=4))

if __name__ == "__main__":
    convert_to_fhir("input.xml")
