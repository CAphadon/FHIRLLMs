import xml.etree.ElementTree as ET

# Read the XML file
tree = ET.parse('patient.xml')

# Convert the XML data into a FHIR JSON resource
fhir_json = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": {
        "resource": {
            "resourceType": "Patient",
            "id": "123456789",
            "subject": {"reference": "patient/123456789"},
            "extension": [
                {"url": "patient/extension/identifier", "value": {"reference": "patient/123456789#identifier"}],
                {"url": "patient/extension/patient_address", "value": {"reference": "patient/123456789#patient_address"}}
            ],
            "data": {
                "name": {"family": ["Max"], "given": ["Mustermann"]},
                "birthDate": "02.04.2023",
                "gender": "M",
                "address": {"line": ["Bahnhofstr. 1"], "city": "Tuebingen", "country": "DE", "postalCode": "70070"}
            }
        }
    }
}

# Print the FHIR JSON resource
print(fhir_json)

