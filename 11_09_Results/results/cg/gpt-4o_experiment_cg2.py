import xml.etree.ElementTree as ET
import json
import hashlib

# Function to generate a SHA-256 ID from a given string
def generate_id(input_string):
    return hashlib.sha256(input_string.encode('utf-8')).hexdigest()

# Parse XML file
tree = ET.parse('input.xml')
root = tree.getroot()

# Extract required fields
namespace = {'ns0': 'http://www.gekid.de/namespace'}
patient = root.find('.//ns0:Patient', namespace)
patient_id = patient.find('.//ns0:Patienten_Stammdaten', namespace).attrib['Patient_ID']
gender = patient.find('.//ns0:Patienten_Geschlecht', namespace).text
birth_date = patient.find('.//ns0:Patienten_Geburtsdatum', namespace).text
address = patient.find('.//ns0:Adresse', namespace)
postal_code = address.find('.//ns0:Patienten_PLZ', namespace).text
country = address.find('.//ns0:Patienten_Land', namespace).text

# Generate FHIR ID
fhir_id = generate_id(patient_id)

# Create FHIR JSON
fhir_json = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": [
        {
            "fullUrl": f"Patient/{fhir_id}",
            "resource": {
                "resourceType": "Patient",
                "id": fhir_id,
                "meta": {
                    "source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test",
                    "profile": [
                        "https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"
                    ]
                },
                "identifier": [
                    {
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue",
                                    "code": "PSEUDED"
                                },
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "MR",
                                    "display": "Medical·record·number"
                                }
                            ]
                        },
                        "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id",
                        "value": patient_id
                    }
                ],
                "gender": "male" if gender == 'M' else "female",
                "birthDate": birth_date.replace('.', '-'),
                "address": [
                    {
                        "type": "both",
                        "postalCode": postal_code,
                        "country": country
                    }
                ]
            },
            "request": {
                "method": "PUT",
                "url": f"Patient/{fhir_id}"
            }
        }
    ]
}

# Print FHIR JSON
print(json.dumps(fhir_json, indent=4))
