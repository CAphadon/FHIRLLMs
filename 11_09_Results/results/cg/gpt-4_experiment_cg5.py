
import json
from xml.etree import ElementTree as ET

def xml_to_json(xml_str):
    root = ET.fromstring(xml_str)
    ns = {'ns0': 'http://www.gekid.de/namespace'}

    patient = root.find('ns0:Menge_Patient/ns0:Patient', ns)
    patient_data = patient.find('ns0:Patienten_Stammdaten', ns)
    patient_id = patient_data.attrib['Patient_ID']
    gender = patient_data.find('ns0:Patienten_Geschlecht', ns).text
    if gender == 'M':
        gender = 'male'
    else:
        gender = 'female'
    birth_date = patient_data.find('ns0:Patienten_Geburtsdatum', ns).text
    birth_date = '-'.join(reversed(birth_date.split('.')))
    first_name = patient_data.find('ns0:Patienten_Vornamen', ns).text
    last_name = patient_data.find('ns0:Patienten_Nachname', ns).text

    fhir_json = {
        "resourceType": "Bundle",
        "type": "transaction",
        "entry": [
            {
                "resource": {
                    "resourceType": "Patient",
                    "id": patient_id,
                    "name": [
                        {
                            "family": last_name,
                            "given": [first_name]
                        },
                    ],
                    "gender": gender,
                    "birthDate": birth_date
                },
                "request": {
                    "method": "POST",
                    "url": "Patient"
                }
            }
        ]
    }
    return json.dumps(fhir_json, indent=2)

# XML data
xml_str = """<ns0:ADT_GEKID xmlns:ns0="http://www.gekid.de/namespace" Schema_Version="2.2.1">
... (The rest of your XML data) ...
</ns0:ADT_GEKID>"""

# Convert XML to JSON
fhir_json = xml_to_json(xml_str)

# Print the resulting FHIR JSON
print(fhir_json)
