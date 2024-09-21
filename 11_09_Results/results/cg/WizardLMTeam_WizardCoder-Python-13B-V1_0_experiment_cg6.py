import json
import xml.etree.ElementTree as ET

input_xml = '''<ns0:ADT_GEKID xmlns:ns0="http://www.gekid.de/namespace" Schema_Version="2.2.1">
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
</ns0:ADT_GEKID>'''

# Parse the input xml
root = ET.fromstring(input_xml)

# Define the mapping from the xml elements to the FHIR resource
mapping = {
    "ns0:Patienten_Nachname": "name[0].family",
    "ns0:Patienten_Vornamen": "name[0].given",
    "ns0:Patienten_Geschlecht": "gender",
    "ns0:Patienten_Geburtsdatum": "birthDate",
    "ns0:Patienten_Strasse": "address[0].line",
    "ns0:Patienten_PLZ": "address[0].postalCode",
    "ns0:Patienten_Land": "address[0].country",
    "ns0:Patient_ID": "identifier[0].value"
}

# Initialize the output json object
output_json = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": [
        {
            "fullUrl": "Patient/d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937",
            "resource": {
                "resourceType": "Patient",
                "id": "d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937",
                "meta": {
                    "source": "99999.ONKOSTAR:obds-to-fhir:0.0.0-test",
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
                        "value": "105555888"
                    }
                ]
            },
            "request": {
                "method": "PUT",
                "url": "Patient/d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937"
            }
        }
    ]
}

# Loop through the input xml and extract the data
for patient in root.findall("ns0:Patient", {"ns0": "http://www.gekid.de/namespace"}):
    for patient_data in patient.findall("ns0:Patienten_Stammdaten", {"ns0": "http://www.gekid.de/namespace"}):
        for key, value in mapping.items():
            if key.startswith("ns0:Patienten_Land"):
                output_json["entry"][0]["resource"]["address"][0]["country"] = patient_data.find(key).text
            elif key.startswith("ns0:Patienten_PLZ"):
                output_json["entry"][0]["resource"]["address"][0]["postalCode"] = patient_data.find(key).text
            elif key.startswith("ns0:Patienten_Strasse"):
                output_json["entry"][0]["resource"]["address"][0]["line"] = patient_data.find(key).text
            elif key.startswith("ns0:Patienten_Nachname"):
                output_json["entry"][0]["resource"]["name"][0]["family"] = patient_data.find(key).text
            elif key.startswith("ns0:Patienten_Vornamen"):
                output_json["entry"][0]["resource"]["name"][0]["given"] = patient_data.find(key).text
            elif key.startswith("ns0:Patient_ID"):
                output_json["entry"][0]["resource"]["identifier"][0]["value"] = patient_data.find(key).text
            elif key.startswith("ns0:Patienten_Geschlecht"):
                gender = patient_data.find(key).text
                if gender == "M":
                    output_json["entry"][0]["resource"]["gender"] = "male"
                elif gender == "W":
                    output_json["entry"][0]["resource"]["gender"] = "female"
                else:
                    output_json["entry"][0]["resource"]["gender"] = "unknown"

print(json.dumps(output_json, indent=2)) 