You are a Python Software Engineer and are asked to create a Python programm that turns the content of a xml file into a specific json. The xml file contains data from a database while the json is supposed to be a FHIR resource json. The input looks like this: 
<ns0:ADT_GEKID xmlns:ns0="http://www.gekid.de/namespace" Schema_Version="2.2.1">
	<ns0:Absender Absender_ID="999999" Software_ID="ONKOSTAR" Installations_ID="2.9.8">
		<ns0:Absender_Bezeichnung>UKER</ns0:Absender_Bezeichnung>
		<ns0:Absender_Ansprechpartner />
		<ns0:Absender_Anschrift>Maximiliansplatz 2, 91054 Erlangen</ns0:Absender_Anschrift>
	</ns0:Absender>
	<ns0:Menge_Patient>
		<ns0:Patient>
            <ns0:Patienten_Stammdaten Patient_ID="1055555888">
                <ns0:KrankenversichertenNr>Q00000000</ns0:KrankenversichertenNr>
                <ns0:KrankenkassenNr>10000000</ns0:KrankenkassenNr>
                <ns0:Patienten_Nachname>Doe</ns0:Patienten_Nachname>
                <ns0:Patienten_Vornamen>John</ns0:Patienten_Vornamen>
                <ns0:Patienten_Geschlecht>M</ns0:Patienten_Geschlecht>
                <ns0:Patienten_Geburtsdatum>11.09.1900</ns0:Patienten_Geburtsdatum>
                <ns0:Menge_Adresse>
                    <ns0:Adresse>
                        <ns0:Patienten_Strasse>Johnstr. 7</ns0:Patienten_Strasse>
                        <ns0:Patienten_Land>DE</ns0:Patienten_Land>
                        <ns0:Patienten_PLZ>91000</ns0:Patienten_PLZ>
                        <ns0:Patienten_Ort>Johncity</ns0:Patienten_Ort>
                    </ns0:Adresse>
                </ns0:Menge_Adresse>
            </ns0:Patienten_Stammdaten>
			<ns0:Menge_Meldung>
				<ns0:Meldung Meldung_ID="ST0001238" Melder_ID="ST">
					<ns0:Meldedatum>10.11.2021</ns0:Meldedatum>
					<ns0:Meldebegruendung>I</ns0:Meldebegruendung>
					<ns0:Meldeanlass>behandlungsende</ns0:Meldeanlass>
					<ns0:Tumorzuordnung Tumor_ID="1">
                        <ns0:Primaertumor_ICD_Code>C72.0</ns0:Primaertumor_ICD_Code>
                        <ns0:Primaertumor_ICD_Version>10 2021 GM</ns0:Primaertumor_ICD_Version>
                        <ns0:Diagnosedatum>18.05.2021</ns0:Diagnosedatum>
                        <ns0:Seitenlokalisation>R</ns0:Seitenlokalisation>
                    </ns0:Tumorzuordnung>
					<ns0:Menge_ST>
						<ns0:ST ST_ID="45900">
							<ns0:ST_Intention>P</ns0:ST_Intention>
							<ns0:ST_Stellung_OP>N</ns0:ST_Stellung_OP>
							<ns0:Menge_Bestrahlung>
								<ns0:Bestrahlung>
									<ns0:ST_Zielgebiet>5.4.-</ns0:ST_Zielgebiet>
									<ns0:ST_Seite_Zielgebiet>T</ns0:ST_Seite_Zielgebiet>
								</ns0:Bestrahlung>
								<ns0:Bestrahlung>
									<ns0:ST_Zielgebiet>1.2</ns0:ST_Zielgebiet>
									<ns0:ST_Seite_Zielgebiet>R</ns0:ST_Seite_Zielgebiet>
									<ns0:ST_Ende_Datum>02.12.2021</ns0:ST_Ende_Datum>
								</ns0:Bestrahlung>
							</ns0:Menge_Bestrahlung>
							<ns0:ST_Ende_Grund>L</ns0:ST_Ende_Grund>
							<ns0:Menge_Nebenwirkung>
								<ns0:ST_Nebenwirkung>
									<ns0:Nebenwirkung_Grad>4</ns0:Nebenwirkung_Grad>
								</ns0:ST_Nebenwirkung>
							</ns0:Menge_Nebenwirkung>
						</ns0:ST>
					</ns0:Menge_ST>
				</ns0:Meldung>
			</ns0:Menge_Meldung>
		</ns0:Patient>
	</ns0:Menge_Patient>
	<ns0:Menge_Melder>
		<ns0:Melder Melder_ID="ST">
			<ns0:Meldende_Stelle>ST</ns0:Meldende_Stelle>
		</ns0:Melder>
	</ns0:Menge_Melder>
</ns0:ADT_GEKID> while the output should look like this: 
{"resourceType": "Bundle", "type": "transaction", "entry": [{"fullUrl": "Patient/d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937", "resource": {"resourceType": "Patient", "id": "d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937", "meta": {"source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test", "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]}, "identifier": [{"type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "PSEUDED"}, {"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical\u00b7record\u00b7number"}]}, "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id", "value": "1055555888"}], "gender": "male", "birthDate": "1900-07", "address": [{"type": "both", "postalCode": "91000", "country": "DE"}]}, "request": {"method": "PUT", "url": "Patient/d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937"}}]}. The runnable python code for this task that only prints the resulting FHIR json to the console looks like this:
```python
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
```
This code takes advantage of the xml.etree.ElementTree module to parse the XML file and iterate through its nodes. It creates FHIR resources based on the structure of the XML and adds them to a FHIR bundle. The resulting FHIR json is then printed to the console.