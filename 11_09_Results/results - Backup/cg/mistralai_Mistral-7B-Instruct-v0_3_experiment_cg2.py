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
{"resourceType": "Bundle", "type": "transaction", "entry": [{"fullUrl": "Patient/d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937", "resource": {"resourceType": "Patient", "id": "d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937", "meta": {"source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test", "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]}, "identifier": [{"type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "PSEUDED"}, {"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical\u00b7record\u00b7number"}]}, "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id", "value": "1055555888"}], "gender": "male", "birthDate": "1900-07", "address": [{"type": "both", "postalCode": "91000", "country": "DE"}]}, "request": {"method": "PUT", "url": "Patient/d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937"}}]}. The resulting FHIR profile is called Person. Create runnable python code for this task that only prints the resulting FHIR json to the console.  Only return the python code!

```python
import xml.etree.ElementTree as ET
import json
from datetime import datetime
from typing import List, Dict, Any, Tuple
from collections import OrderedDict

def xml_to_dict(xml_node: ET.Element):
    dict_ = {}
    for key, value in xml_node.attrib.items():
        dict_[key] = value
    children = list(xml_node)
    if children:
        dict_[key] = [xml_to_dict(child) for child in children]
    else:
        dict_[key] = xml_node.text
    return dict_

def create_fhir_person(patient_data: dict) -> Dict[str, Any]:
    fhir_person = OrderedDict()
    fhir_person["resourceType"] = "Patient"
    fhir_person["id"] = patient_data["KrankenversichertenNr"]
    fhir_person["meta"] = {
        "source": f"{patient_data['Absender_ID']}.{patient_data['Software_ID']}:obds-to-fhir:0.0.0-test",
        "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]
    }
    identifier = {}
    identifier["type"] = {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "PSEUDED"}, {"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical\u00b7record\u00b7number"}]}
    identifier["system"] = "https://fhir.diz.uk-erlangen.de/identifiers/patient-id"
    identifier["value"] = patient_data["KrankenversichertenNr"]
    fhir_person["identifier"] = [identifier]
    fhir_person["gender"] = "male"
    birth_date = patient_data["Patienten_Geburtsdatum"].split(".")
    fhir_person["birthDate"] = f"{birth_date[2]}-{birth_date[1]}-{birth_date[0]}"
    address = {}
    address["type"] = "both"
    address["postalCode"] = patient_data["Patienten_PLZ"]
    address["country"] = "DE"
    fhir_person["address"] = [address]
    return fhir_person

def main():
    xml_data = """<ns0:ADT_GEKID xmlns:ns0="http://www.gekid.de/namespace" Schema_Version="2.2.1">
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
    patient_data = xml_to_dict(ET.fromstring(xml_data))
    fhir_bundle = {"resourceType": "Bundle", "type": "transaction", "entry": []}
    fhir_bundle["entry"].append({"fullUrl": f"Patient/{patient_data['KrankenversichertenNr']}", "resource": create_fhir_person(patient_data)})
    print(json.dumps(fhir_bundle, indent=4))

if __name__ == "__main__":
    main()
```