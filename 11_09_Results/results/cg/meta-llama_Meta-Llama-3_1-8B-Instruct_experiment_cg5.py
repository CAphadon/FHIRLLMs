import xml.etree.ElementTree as ET
import json
import fhir

def convert_xml_to_fhir(xml_string):
    root = ET.fromstring(xml_string)
    patient = root.find(".//ns0:Patienten_Stammdaten")
    patient_id = patient.find(".//ns0:Patient_ID").text
    patient_name = patient.find(".//ns0:Patienten_Nachname").text
    patient_given_name = patient.find(".//ns0:Patienten_Vornamen").text
    patient_birth_date = patient.find(".//ns0:Patienten_Geburtsdatum").text
    patient_gender = patient.find(".//ns0:Patienten_Geschlecht").text
    patient_insurer_number = patient.find(".//ns0:KrankenversichertenNr").text
    patient_insurance_number = patient.find(".//ns0:KrankenkassenNr").text

    patient_address = {
        "address": {
            "city": patient.find(".//ns0:Patienten_Ort").text,
            "country": "Germany",
            "postalCode": patient.find(".//ns0:Patienten_PLZ").text,
            "state": "",
            "line": [patient.find(".//ns0:Patienten_Strasse").text],
            "use": "home"
        }
    }

    patient_json = {
        "resourceType": "Patient",
        "id": patient_id,
        "birthDate": patient_birth_date,
        "name": [{"text": f"{patient_name} {patient_given_name}"}],
        "gender": patient_gender,
        "address": patient_address,
        "identifier": [
            {
                "system": "https://fhir.geid.de/namespace/gekid",
                "value": patient_insurer_number,
                "type": "http://terminology.hl7.org/specializations/insurance"
            },
            {
                "system": "https://fhir.geid.de/namespace/gekid",
                "value": patient_insurance_number,
                "type": "http://terminology.hl7.org/specializations/insurance"
            }
        ]
    }

    bundle = {
        "resourceType": "Bundle",
        "type": "transaction",
        "entry": [{"resource": patient_json}]
    }

    return json.dumps(bundle, indent=4)

xml_string = """... the xml string from above"""
print(convert_xml_to_fhir(xml_string))