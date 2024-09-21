
import xml.etree.ElementTree as ET
import json
import hashlib

def parse_patient(patient):
    # Extract patient information from xml data
    patient_id = patient.find('ns0:Patienten_Stammdaten', ns).attrib['Patient_ID']
    patient_gender = patient.find('ns0:Patienten_Stammdaten/ns0:Patienten_Geschlecht', ns).text
    patient_birthdate = patient.find('ns0:Patienten_Stammdaten/ns0:Patienten_Geburtsdatum', ns).text
    patient_address = patient.find('ns0:Patienten_Stammdaten/ns0:Menge_Adresse/ns0:Adresse', ns)
    patient_postalCode = patient_address.find('ns0:Patienten_PLZ', ns).text
    patient_country = patient_address.find('ns0:Patienten_Land', ns).text

    # Convert patient information to FHIR json
    patient_resource = {
        "resourceType": "Patient",
        "id": hashlib.sha256(patient_id.encode()).hexdigest(),
        "meta": {
            "source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test",
            "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]
        },
        "identifier": [
            {
                "type": {
                    "coding": [
                        {"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "PSEUDED"},
                        {"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical record number"}
                    ]
                },
                "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id",
                "value": patient_id
            }
        ],
        "gender": "male" if patient_gender == 'M' else 'female',
        "birthDate": '-'.join(patient_birthdate.split('.')[::-1][1:]),
        "address": [
            {
                "type": "both",
                "postalCode": patient_postalCode,
                "country": patient_country
            }
        ]
    }

    return {"fullUrl": f'Patient/{patient_resource["id"]}', "resource": patient_resource, "request": {"method": "PUT", "url": f'Patient/{patient_resource["id"]}'}}

# Define the xml namespaces
ns = {'ns0': 'http://www.gekid.de/namespace'}

# Parse the xml file
tree = ET.parse('test.xml')
root = tree.getroot()

# Extract patient data from xml and convert to FHIR json
patients = root.findall('ns0:Menge_Patient/ns0:Patient', ns)
patient_bundles = [parse_patient(patient) for patient in patients]

# Build the FHIR bundle
fhir_bundle = {"resourceType": "Bundle", "type": "transaction", "entry": patient_bundles}

# Print the FHIR bundle as json
print(json.dumps(fhir_bundle, indent=2))
