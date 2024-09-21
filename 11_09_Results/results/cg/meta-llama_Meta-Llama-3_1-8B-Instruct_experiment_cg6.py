from lxml import etree
import json

# Define the namespace mappings
ns = {"ns0": "http://www.gekid.de/namespace"}

# Parse the XML file
tree = etree.parse("input.xml")
root = tree.getroot()

# Extract the patient data
patients = []
for patient_node in root.findall(".//ns0:Menge_Patient/ns0:Patient", ns):
    patient_id = patient_node.find(".//ns0:Patienten_Stammdaten/ns0:Patient_ID", ns).text
    patient_name = patient_node.find(".//ns0:Patienten_Nachname", ns).text
    patient_birthdate = patient_node.find(".//ns0:Patienten_Geburtsdatum", ns).text
    patient_gender = patient_node.find(".//ns0:Patienten_Geschlecht", ns).text

    # Extract the address data
    address_street = patient_node.find(".//ns0:Patienten_Strasse", ns).text
    address_postal_code = patient_node.find(".//ns0:Patienten_PLZ", ns).text
    address_country = patient_node.find(".//ns0:Patienten_Land", ns).text

    # Create the FHIR patient resource
    patient = {
        "resourceType": "Patient",
        "id": patient_id,
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
                        {"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "PSEUDED"},
                        {"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical·record·number"}
                    ]
                },
                "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id",
                "value": patient_id
            }
        ],
        "name": [{"family": patient_name}],
        "gender": patient_gender,
        "birthDate": patient_birthdate,
        "address": [
            {
                "type": "both",
                "postalCode": address_postal_code,
                "country": address_country
            }
        ]
    }

    # Extract the Meldung data
    meldungen = []
    for meldung_node in patient_node.findall(".//ns0:Menge_Meldung/ns0:Meldung", ns):
        meldung_id = meldung_node.find(".//ns0:Meldung_ID", ns).text
        meldung_date = meldung_node.find(".//ns0:Meldedatum", ns).text
        meldung_reason = meldung_node.find(".//ns0:Meldebegruendung", ns).text
        meldung_cause = meldung_node.find(".//ns0:Meldeanlass", ns).text

        # Create the FHIR Meldung resource
        meldung = {
            "resourceType": "Meldung",
            "id": meldung_id,
            "meta": {
                "source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test",
                "profile": [
                    "https://www.medizininformatik-initiative.de/fhir/core/modul-meldung/StructureDefinition/MeldungPseudonymisiert"
                ]
            },
            "identifier": [
                {
                    "type": {
                        "coding": [
                            {"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "PSEUDED"},
                            {"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical·record·number"}
                        ]
                    },
                    "system": "https://fhir.diz.uk-erlangen.de/identifiers/meldung-id",
                    "value": meldung_id
                }
            ],
            "date": meldung_date,
            "reason": meldung_reason,
            "cause": meldung_cause
        }

        meldungen.append(meldung)

    # Create the FHIR patient resource with Meldung resources
    patient["meta"]["extension"] = [
        {"url": "http://hl7.org/fhir/StructureDefinition/patient-meldung", "valueBundle": {"entry": meldungen}}
    ]

    patients.append(patient)

# Create the FHIR bundle resource
bundle = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": [
        {
            "fullUrl": f"Patient/{patient_id}",
            "resource": patient,
            "request": {
                "method": "PUT",
                "url": f"Patient/{patient_id}"
            }
        }
    ]
}

# Print the FHIR bundle resource
print(json.dumps(bundle, indent=4))
