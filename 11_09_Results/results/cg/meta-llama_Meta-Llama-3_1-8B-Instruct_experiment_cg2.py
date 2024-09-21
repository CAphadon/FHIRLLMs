import xml.etree.ElementTree as ET
import json

# XML parsing
xml_string = """
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
</ns0:ADT_GEKID>
"""

# Parse XML string into an ElementTree object
root = ET.fromstring(xml_string)

# Extract relevant data from XML
patient_id = root.find(".//ns0:Patienten_Stammdaten/ns0:Patient_ID").text
patient_name = root.find(".//ns0:Patienten_Stammdaten/ns0:Patienten_Nachname").text
patient_birthdate = root.find(".//ns0:Patienten_Stammdaten/ns0:Patienten_Geburtsdatum").text
patient_gender = root.find(".//ns0:Patienten_Stammdaten/ns0:Patienten_Geschlecht").text
patient_address = {
    "type": "both",
    "postalCode": root.find(".//ns0:Patienten_Stammdaten/ns0:Menge_Adresse/ns0:Adresse/ns0:Patienten_PLZ").text,
    "country": root.find(".//ns0:Patienten_Stammdaten/ns0:Menge_Adresse/ns0:Adresse/ns0:Patienten_Land").text
}

# Create FHIR resource
fhir_resource = {
    "resourceType": "Patient",
    "id": patient_id,
    "meta": {
        "source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test",
        "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]
    },
    "identifier": [
        {
            "type": {
                "coding": [
                    {"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "PSEUDED"},
                    {"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical\u00b7record\u00b7number"}
                ]
            },
            "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id",
            "value": patient_id
        }
    ],
    "name": [{"text": patient_name}],
    "gender": patient_gender,
    "birthDate": patient_birthdate,
    "address": [patient_address]
}

# Create Bundle
bundle = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": [
        {
            "fullUrl": f"Patient/{patient_id}",
            "resource": fhir_resource,
            "request": {
                "method": "PUT",
                "url": f"Patient/{patient_id}"
            }
        }
    ]
}

# Print Bundle to console
print(json.dumps(bundle, indent=4))