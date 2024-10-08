```python
import xml.etree.ElementTree as ET
import json

# Parse the XML file
tree = ET.parse('input.xml')
root = tree.getroot()

# Create the FHIR resource json
fhir_json = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": [{
        "fullUrl": "Patient/d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937",
        "resource": {
            "resourceType": "Patient",
            "id": "d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937",
            "meta": {
                "source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test",
                "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]
            },
            "identifier": [{
                "type": {
                    "coding": [{
                        "system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue",
                        "code": "PSEUDED"
                    }, {
                        "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                        "code": "MR",
                        "display": "Medical record number"
                    }]
                },
                "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id",
                "value": "1055555888"
            }],
            "gender": "male",
            "birthDate": "1900-07",
            "address": [{
                "type": "both",
                "postalCode": "91000",
                "country": "DE"
            }]
        },
        "request": {
            "method": "PUT",
            "url": "Patient/d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937"
        }
    }]
}

# Print the FHIR resource json
print(json.dumps(fhir_json))
```