import xml.etree.ElementTree as ET
import json

# Parse the XML file
tree = ET.parse('input.xml')
root = tree.getroot()

# Create a dictionary to store the FHIR resources
fhir_resources = {}

# Iterate over the Patient elements
for patient in root.findall('.//ns0:Menge_Patient/ns0:Patient'):
    # Extract the patient data
    patient_id = patient.find('ns0:Patienten_Stammdaten/ns0:KrankenversichertenNr').text
    first_name = patient.find('ns0:Patienten_Vornamen').text
    last_name = patient.find('ns0:Patienten_Nachname').text
    birth_date = patient.find('ns0:Patienten_Geburtsdatum').text
    gender = patient.find('ns0:Patienten_Geschlecht').text
    address = patient.find('ns0:Menge_Adresse/ns0:Adresse')

    # Create the FHIR Patient resource
    patient_resource = {
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
        "name": [
            {
                "family": last_name,
                "given": first_name
            }
        ],
        "gender": gender,
        "birthDate": birth_date,
        "address": [
            {
                "type": "both",
                "postalCode": address.find('ns0:Patienten_PLZ').text,
                "country": address.find('ns0:Patienten_Land').text
            }
        ]
    }

    # Add the patient resource to the list of FHIR resources
    fhir_resources[patient_id] = patient_resource

    # Iterate over the Meldung elements
    for meldung in patient.findall('.//ns0:Menge_Meldung/ns0:Meldung'):
        # Extract the Meldung data
        meldung_id = meldung.find('ns0:Meldung_ID').text
        meldebegruendung = meldung.find('ns0:Meldebegruendung').text
        meldeanlass = meldung.find('ns0:Meldeanlass').text
        tumor_id = meldung.find('ns0:Tumorzuordnung/ns0:Primaertumor_ICD_Code').text
        diagnosedatum = meldung.find('ns0:Tumorzuordnung/ns0:Diagnosedatum').text

        # Create the FHIR Observation resource
        observation_resource = {
            "resourceType": "Observation",
            "id": meldung_id,
            "meta": {
                "source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test",
                "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-observation/StructureDefinition/ObservationPseudonymisiert"]
            },
            "identifier": [
                {
                    "type": {
                        "coding": [
                            {"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "PSEUDED"},
                            {"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical\u00b7record\u00b7number"}
                        ]
                    },
                    "system": "https://fhir.diz.uk-erlangen.de/identifiers/observation-id",
                    "value": meldung_id
                }
            ],
            "subject": {"reference": "Patient/" + patient_id},
            "category": "social-determinant-of-health",
            "code": {"coding": [{"system": "http://snomed.info/sct", "code": tumor_id, "display": tumor_id}]},
            "effective": diagnosedatum,
            "valueCodeableConcept": {"coding": [{"system": "http://snomed.info/sct", "code": meldeanlass, "display": meldeanlass}]}
        }

        # Add the observation resource to the list of FHIR resources
        fhir_resources[meldung_id] = observation_resource

# Create the FHIR Bundle resource
bundle_resource = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": []
}

# Iterate over the FHIR resources
for resource_id, resource in fhir_resources.items():
    # Add the resource to the Bundle
    bundle_resource["entry"].append({
        "fullUrl": "Patient/" + resource_id,
        "resource": resource
    })

# Print the FHIR Bundle resource as JSON
print(json.dumps(bundle_resource, indent=4))