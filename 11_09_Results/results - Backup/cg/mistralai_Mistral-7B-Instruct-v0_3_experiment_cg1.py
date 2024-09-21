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
{"resourceType": "Bundle", "type": "transaction", "entry": [{"fullUrl": "Patient/d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937", "resource": {"resourceType": "Patient", "id": "d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937", "meta": {"source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test", "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]}, "identifier": [{"type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "PSEUDED"}, {"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical\u00b7record\u00b7number"}]}, "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id", "value": "1055555888"}], "gender": "male", "birthDate": "1900-07", "address": [{"type": "both", "postalCode": "91000", "country": "DE"}]}, "request": {"method": "PUT", "url": "Patient/d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937"}}]}. Create runnable python code for this task that only prints the resulting FHIR json to the console. Only return the python code!

```python
import xml.etree.ElementTree as ET
import json
from datetime import datetime
from typing import List, Dict, Any
from fhir.resources.patient import Patient
from fhir.resources.observation import Observation

def parse_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%d.%m.%Y")

def get_patient_id(identifier: List[Dict[str, Any]]) -> str:
    for ident in identifier:
        if ident["type"][0]["code"] == "MR":
            return ident["value"]
    return ""

def parse_address(address_str: str) -> Dict[str, Any]:
    address = {"type": "both", "postalCode": "", "country": ""}
    address_parts = address_str.split(", ")
    address["postalCode"] = address_parts[0].strip()
    address["country"] = address_parts[1].strip()
    return address

def parse_patient(absender: ET.Element) -> Patient:
    patient = Patient()
    patient.id = get_patient_id(absender.findall(".//ns0:Patienten_Stammdaten/@patient_id"))
    patient.meta.source = absender.find(".//ns0:Absender/@Software_ID").text + ":" + absender.find(".//ns0:ADT_GEKID/@Schema_Version").text + ":obds-to-fhir:0.0.0-test"
    patient.meta.profile = [
        "https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"
    ]
    for child in absender.findall(".//ns0:Patienten_Stammdaten"):
        if child.tag == "ns0:KrankenversichertenNr":
            patient.identifier.append(
                Observation(
                    value=[Patient.identifier_type_system_MR, Patient.identifier_type_value(child.text)]
                )
            )
        if child.tag == "ns0:Patienten_Nachname":
            patient.name.family = child.text
        if child.tag == "ns0:Patienten_Vornamen":
            patient.name.given = [child.text]
        if child.tag == "ns0:Patienten_Geschlecht":
            patient.gender = child.text
        if child.tag == "ns0:Patienten_Geburtsdatum":
            patient.birthDate = parse_date(child.text)
        if child.tag == "ns0:Menge_Adresse":
            address = child.find(".//ns0:Adresse")
            patient.address.append(parse_address(address.get(f"{ns0}:{address.get('Patienten_Strasse')}")))
    return patient

def parse_resource(adt_gekid: ET.Element) -> str:
    bundle = {"resourceType": "Bundle", "type": "transaction", "entry": []}
    for patient in adt_gekid.findall(".//ns0:Menge_Patient/ns0:Patient"):
        patient_json = patient.find(".//ns0:Patienten_Stammdaten").toxml("json", cls=PatientJsonNamespace)
        patient_json = json.loads(patient_json)
        patient_json["resourceType"] = "Patient"
        bundle["entry"].append(
            {
                "fullUrl": f"Patient/{patient_json['id']}",
                "resource": patient_json,
            }
        )
        request = {"method": "PUT", "url": f"Patient/{patient_json['id']}"}
        bundle["entry"].append({"request": request})
    return json.dumps(bundle)

if __name__ == "__main__":
    ns0 = {"ns0": "http://www.gekid.de/namespace"}
    xml_str = """<ns0:ADT_GEKID xmlns:ns0="http://www.gekid.de/namespace" Schema_Version="2.2.1">
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
    </ns0:ADT_GEKID>"""
    root = ET.fromstring(xml_str)
    print(parse_resource(root))
```

Note that the code uses the `fhir` library for Python to create FHIR resources. You can install it using `pip install fhir`. Also, the code uses the `xml.etree.ElementTree` module for parsing the XML file.

In this code, the `parse_date` function is used to parse dates in the format "DD.MM.YYYY". The `get_patient_id` function is used to get the patient ID from the XML data. The `parse_address` function is used to parse the address data from the XML data. The `parse_patient` function is used to parse a single patient from the XML data and convert it to a FHIR `Patient` resource. The `parse_resource` function is used to parse the entire XML data and convert it to a FHIR `Bundle` resource. Finally, the main part of the code uses these functions to parse the XML data and print the resulting FHIR JSON to the console.