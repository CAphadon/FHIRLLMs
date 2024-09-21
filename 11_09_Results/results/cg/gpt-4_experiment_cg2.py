import xmltodict
import json

def convert_xml_to_json(file_path):
    with open(file_path, 'r') as file:
        xml_content = file.read()
    dict_content = xmltodict.parse(xml_content)
    json_content = convert_to_fhir_json(dict_content)
    print(json_content)

def convert_to_fhir_json(dict_content):
    patient_data = dict_content["ns0:ADT_GEKID"]["ns0:Menge_Patient"]["ns0:Patient"]["ns0:Patienten_Stammdaten"]
    patient_address = patient_data["ns0:Menge_Adresse"]["ns0:Adresse"]
    sender_data = dict_content["ns0:ADT_GEKID"]["ns0:Absender"]
    gender = "male" if patient_data["ns0:Patienten_Geschlecht"] == "M" else "female"

    json_data = {
        "resourceType": "Bundle",
        "type": "transaction",
        "entry": [{
            "fullUrl": "Patient/d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937",
            "resource": {
                "resourceType": "Patient",
                "id": "d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937",
                "meta": {
                    "source": f'{sender_data["Absender_ID"]}.{sender_data["Software_ID"]}:obds-to-fhir:0.0.0-test',
                    "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]
                },
                "identifier": [{
                    "type": {
                        "coding": [
                            {"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "PSEUDED"},
                            {"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical\u00b7record\u00b7number"}
                        ]
                    },
                    "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id",
                    "value": patient_data["Patient_ID"]
                }],
                "gender": gender,
                "birthDate": patient_data["ns0:Patienten_Geburtsdatum"].replace('.', '-'),
                "address": [{
                    "type": "both",
                    "postalCode": patient_address["ns0:Patienten_PLZ"],
                    "country": patient_address["ns0:Patienten_Land"]
                }]
            },
            "request": {
                "method": "PUT",
                "url": "Patient/d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937"
            }
        }]
    }
    return json.dumps(json_data)

# Call the function with the path to the XML file
# convert_xml_to_json('path_to_your_xml_file.xml')
