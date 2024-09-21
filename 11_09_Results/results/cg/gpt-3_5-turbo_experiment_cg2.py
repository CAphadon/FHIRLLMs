import xml.etree.ElementTree as ET
import json

# Parse the xml file
tree = ET.parse('input.xml')
root = tree.getroot()

# Define the FHIR resource json structure
fhir_json = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": []
}

# Extract data from the xml file and populate the FHIR json structure
patient_id = root.find('.//{http://www.gekid.de/namespace}Patienten_Stammdaten').attrib['Patient_ID']
gender = root.find('.//{http://www.gekid.de/namespace}Patienten_Geschlecht').text
birthdate = root.find('.//{http://www.gekid.de/namespace}Patienten_Geburtsdatum').text
postal_code = root.find('.//{http://www.gekid.de/namespace}Patienten_PLZ').text
country = root.find('.//{http://www.gekid.de/namespace}Patienten_Land').text

fhir_entry = {
    "fullUrl": f"Patient/{patient_id}",
    "resource": {
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
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue",
                            "code": "PSEUDED"
                        },
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                            "code": "MR",
                            "display": "Medical record number"
                        }
                    ]
                },
                "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id",
                "value": patient_id
            }
        ],
        "gender": "male" if gender == "M" else "female",  # Assuming M is for male and F is for female
        "birthDate": f"{birthdate[:6]}01",  # Assuming the birthdate format is DD.MM.YYYY
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
        "url": f"Patient/{patient_id}"
    }
}

fhir_json["entry"].append(fhir_entry)

# Convert the FHIR json to string and print it
print(json.dumps(fhir_json))