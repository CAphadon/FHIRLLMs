Here is a Python program that reads an XML file, parses it, and converts the data into a FHIR JSON format. The program uses the `xml.etree.ElementTree` module for parsing XML and the `json` module for generating JSON output.

```python
import xml.etree.ElementTree as ET
import json
import hashlib

def generate_fhir_json(xml_content):
    # Parsing the XML content from a string
    root = ET.fromstring(xml_content)
    
    # Extract relevant information
    absender = root.find('.//{http://www.gekid.de/namespace}Absender')
    patient = root.find('.//{http://www.gekid.de/namespace}Patient')
    patienten_stammdaten = patient.find('.//{http://www.gekid.de/namespace}Patienten_Stammdaten')
    
    # Get Patient ID and hash it to create a unique resource ID
    patient_id = patienten_stammdaten.get('Patient_ID')
    hash_obj = hashlib.sha256(patient_id.encode())
    patient_hash_id = hash_obj.hexdigest()
    
    # Create FHIR JSON structure
    fhir_json = {
        "resourceType": "Bundle",
        "type": "transaction",
        "entry": [
            {
                "fullUrl": f"Patient/{patient_hash_id}",
                "resource": {
                    "resourceType": "Patient",
                    "id": patient_hash_id,
                    "meta": {
                        "source": f"{absender.get('Absender_ID')}.{absender.get('Software_ID')}:obds-to-fhir:0.0.0-test",
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
                                        "display": "Medical record number"
                                    }
                                ]
                            },
                            "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id",
                            "value": patient_id
                        }
                    ],
                    "gender": "male" if patienten_stammdaten.find('.//{http://www.gekid.de/namespace}Patienten_Geschlecht').text == 'M' else "female",
                    "birthDate": patienten_stammdaten.find('.//{http://www.gekid.de/namespace}Patienten_Geburtsdatum').text.replace('.', '-'),
                    "address": [
                        {
                            "type": "both",
                            "postalCode": patienten_stammdaten.find('.//{http://www.gekid.de/namespace}Patienten_PLZ').text,
                            "country": patienten_stammdaten.find('.//{http://www.gekid.de/namespace}Patienten_Land').text
                        }
                    ]
                },
                "request": {
                    "method": "PUT",
                    "url": f"Patient/{patient_hash_id}"
                }
            }
        ]
    }
    
    # Convert the dictionary to JSON and print it
    print(json.dumps(fhir_json, indent=4))

# Sample XML content (in practice, this would be read from a file or another source)
xml_content = '''
<ns0:ADT_GEKID xmlns:ns0="http://www.gekid.de/namespace" Schema_Version="2.2.1">
    <!-- XML content here -->
</ns0:ADT_GEKID>
'''

# Call the function to generate FHIR JSON
generate_fhir_json(xml_content)
```

Note:
- This example assumes that the XML namespaces and paths used in `find()` methods match your actual XML. You might need to adjust them according to your XML structure.
- It's essential to inspect the XML structure and ensure that the paths are correctly defined.
- In production, you should handle potential `None` values that might occur if an element is missing in the XML, to avoid `AttributeError`.