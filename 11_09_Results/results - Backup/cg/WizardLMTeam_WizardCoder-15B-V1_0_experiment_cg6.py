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
import xmltodict
import json

with open('input.xml', 'r') as f:
    xml_string = f.read()

xml_dict = xmltodict.parse(xml_string)

# convert xml to fhir json
fhir_json = {"resourceType": "Bundle", "type": "transaction", "entry": []}

# loop through patients and melds
for patient in xml_dict['ns0:ADT_GEKID']['ns0:Menge_Patient']['ns0:Patient']:
    patient_id = patient['ns0:Patienten_Stammdaten']['@Patient_ID']
    krankenversichertenNr = patient['ns0:Patienten_Stammdaten']['ns0:KrankenversichertenNr']
    krankenkassenNr = patient['ns0:Patienten_Stammdaten']['ns0:KrankenkassenNr']
    patient_nachname = patient['ns0:Patienten_Stammdaten']['ns0:Patienten_Nachname']
    patient_vornamen = patient['ns0:Patienten_Stammdaten']['ns0:Patienten_Vornamen']
    patient_geschlecht = patient['ns0:Patienten_Stammdaten']['ns0:Patienten_Geschlecht']
    patient_geburtsdatum = patient['ns0:Patienten_Stammdaten']['ns0:Patienten_Geburtsdatum']
    adresse_strasse = patient['ns0:Menge_Adresse']['ns0:Adresse']['ns0:Patienten_Strasse']
    adresse_land = patient['ns0:Menge_Adresse']['ns0:Adresse']['ns0:Patienten_Land']
    adresse_plz = patient['ns0:Menge_Adresse']['ns0:Adresse']['ns0:Patienten_PLZ']
    adresse_ort = patient['ns0:Menge_Adresse']['ns0:Adresse']['ns0:Patienten_Ort']

    patient_json = {"resourceType": "Patient", "id": patient_id, "meta": {"source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test", "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]}, "identifier": [{"type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "PSEUDED"}, {"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical\u00b7record\u00b7number"}]}, "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id", "value": patient_id}], "gender": patient_geschlecht, "birthDate": patient_geburtsdatum, "address": [{"type": "both", "postalCode": adresse_plz, "country": adresse_land, "line": [adresse_strasse], "city": adresse_ort}]}

    # loop through melds
    for meldung in patient['ns0:Menge_Meldung']['ns0:Meldung']:
        meldung_id = meldung['@Meldung_ID']
        melder_id = meldung['@Melder_ID']
        meldedatum = meldung['ns0:Meldedatum']
        meldebegruendung = meldung['ns0:Meldebegruendung']
        meldeanlass = meldung['ns0:Meldeanlass']

        # loop through tumors
        tumor_id = meldung['ns0:Tumorzuordnung']['@Tumor_ID']
        primaertumor_icd_code = meldung['ns0:Tumorzuordnung']['ns0:Primaertumor_ICD_Code']
        primaertumor_icd_version = meldung['ns0:Tumorzuordnung']['ns0:Primaertumor_ICD_Version']
        diagnosedatum = meldung['ns0:Tumorzuordnung']['ns0:Diagnosedatum']
        seitenlokalisation = meldung['ns0:Tumorzuordnung']['ns0:Seitenlokalisation']

        # add patient reference to tumor
        tumor_json = {"resourceType": "Observation", "id": tumor_id, "meta": {"source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test", "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-observation/StructureDefinition/ObservationTumor"]}, "status": "final", "category": [{"coding": [{"system": "http://terminology.hl7.org/CodeSystem/observation-category", "code": "laboratory", "display": "Laboratory"}]}], "code": {"coding": [{"system": "http://www.icd10data.com/icd10pcs", "code": primaertumor_icd_code, "version": primaertumor_icd_version}]}, "subject": {"reference": f"Patient/{patient_id}"}, "valueCodeableConcept": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "C72.0", "display": "Tumor of colon"}]}, "effectiveDateTime": diagnosedatum}

        # loop through sts
        for st in meldung['ns0:Menge_ST']['ns0:ST']:
            st_id = st['@ST_ID']
            st_intention = st['ns0:ST_Intention']
            st_stellung_op = st['ns0:ST_Stellung_OP']

            # loop through bestrahlungen
            bestrahlungen_json = []
            for bestrahlung in st['ns0:Menge_Bestrahlung']['ns0:Bestrahlung']:
                st_zielgebiet = bestrahlung['ns0:ST_Zielgebiet']
                st_seite_zielgebiet = bestrahlung['ns0:ST_Seite_Zielgebiet']
                if 'ns0:ST_Ende_Datum' in bestrahlung:
                    st_ende_datum = bestrahlung['ns0:ST_Ende_Datum']
                else:
                    st_ende_datum = diagnosedatum

                bestrahlungen_json.append({"resourceType": "Procedure", "id": f"{st_id}-{str(len(bestrahlungen_json))}", "meta": {"source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test", "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-operation/StructureDefinition/OperationBestrahlung"]}, "status": "completed", "category": [{"coding": [{"system": "http://terminology.hl7.org/CodeSystem/procedure-category", "code": "114005", "display": "Bestrahlung"}]}], "code": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/snomed-ct", "code": "40646007", "display": "Therapeutic agent (substance) for surgical operation on tissue"}]}, "subject": {"reference": f"Patient/{patient_id}"}, "performedDateTime": st_ende_datum, "outcome": {"text": f"Zielgebiet {st_zielgebiet} Seite {st_seite_zielgebiet}, Ende {st_ende_datum}"} })

            # loop through nebenwirkungen
            nebenwirkungen_json = []
            for nebenwirkung in st['ns0:Menge_Nebenwirkung']['ns0:ST_Nebenwirkung']:
                nebenwirkung_grad = nebenwirkung['ns0:Nebenwirkung_Grad']
                nebenwirkungen_json.append({"resourceType": "DiagnosticReport", "id": f"{st_id}-{str(len(nebenwirkungen_json))}", "meta": {"source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test", "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-diagnostischer-bericht/StructureDefinition/DiagnosticReportNebenwirkung"]}, "status": "final", "code": {"coding": [{"system": "http://snomed.info/sct", "code": "69930003", "display": "Nebenwirkung des Therapieausweises"}]}, "subject": {"reference": f"Patient/{patient_id}"}, "effectiveDateTime": diagnosedatum, "result": [{"reference": f"Observation/{tumor_id}"}], "interpretation": [{"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation", "code": f"H{nebenwirkung_grad}", "display": f"{nebenwirkung_grad}-stufige Nebenwirkung"}]}, {"text": f"{nebenwirkung_grad}-stufige Nebenwirkung"}]})

            # add st and nebenwirkungen to meldung
            st_json = {"resourceType": "ServiceRequest", "id": st_id, "meta": {"source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test", "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-operation/StructureDefinition/OperationST"]}, "status": "completed", "intent": "order", "code": {"coding": [{"system": "http://snomed.info/sct", "code": "18340000", "display": "Operation on stomach (procedure)"}]}, "subject": {"reference": f"Patient/{patient_id}"}, "occurrenceDateTime": meldedatum, "reasonReference": [{"reference": f"DiagnosticReport/{nebenwirkungen_json[0]['id']}"}]})

            # add meldung, tumor, st, and bestrahlungen to patient
            patient_json["carePlan"] = {"reference": f"ServiceRequest/{st_id}"}
            patient_json["extension"] = [{"url": "http://fhir-registry.smarthealthit.org/StructureDefinition/related-condition", "valueReference": {"reference": f"Condition/Condition-{meldung_id}"}}]
            patient_json["extension"].append({"url": "http://fhir-registry.smarthealthit.org/StructureDefinition/related-procedure", "valueReference": {"reference": f"ServiceRequest/{st_id}"}})
            patient_json["extension"].append({"url": "http://fhir-registry.smarthealthit.org/StructureDefinition/related-observation", "valueReference": {"reference": f"Observation/{tumor_id}"}})
            patient_json.update({"entry": [{"fullUrl": f"Patient/{patient_id}", "resource": patient_json}, {"fullUrl": f"ServiceRequest/{st_id}", "resource": st_json}, {"fullUrl": f"DiagnosticReport/{nebenwirkungen_json[0]['id']}", "resource": nebenwirkungen_json[0]}, {"fullUrl": f"Observation/{tumor_id}", "resource": tumor_json}]})

            # add meldung, tumor, st, and bestrahlungen to fhir json
            fhir_json["entry"].append({"fullUrl": f"Condition/Condition-{meldung_id}", "resource": {"resourceType": "Condition", "id": meldung_id, "meta": {"source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test", "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-gesundheitszustand/StructureDefinition/ConditionMeldepflicht"]}, "code": {"coding": [{"system": "http://snomed.info/sct", "code": "16266005", "display": "Meldepflicht (Krankheit)"}]}, "subject": {"reference": f"Patient/{patient_id}"}, "onsetDateTime": diagnosedatum}})
            fhir_json["entry"].append({"fullUrl": f"ServiceRequest/{st_id}", "resource": st_json})
            fhir_json["entry"].append({"fullUrl": f"DiagnosticReport/{nebenwirkungen_json[0]['id']}", "resource": nebenwirkungen_json[0]})
            fhir_json["entry"].append({"fullUrl": f"Observation/{tumor_id}", "resource": tumor_json})
            fhir_json["entry"].append({"fullUrl": f"Procedure/{bestrahlungen_json[0]['id']}", "resource": bestrahlungen_json[0]})
            for i in range(1, len(bestrahlungen_json)):
                fhir_json["entry"].append({"fullUrl": f"Procedure/{bestrahlungen_json[i]['id']}", "resource": bestrahlungen_json[i]})
            for i in range(len(nebenwirkungen_json)):
                if i!= 0:
                    fhir_json["entry"].append({"fullUrl": f"DiagnosticReport/{nebenwirkungen_json[i]['id']}", "resource": nebenwirkungen_json[i]})

print(json.dumps(fhir_json, indent=4))
```

The resulting json can be pasted into a FHIR server for further processing. Note that this is just a starting point and further development and testing is needed to ensure the output is correct and complete.