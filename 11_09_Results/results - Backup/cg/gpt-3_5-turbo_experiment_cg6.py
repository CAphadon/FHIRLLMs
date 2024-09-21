```python
import xml.etree.ElementTree as ET
import json

# Load the XML file
tree = ET.parse('input.xml')
root = tree.getroot()

# Extract data from XML and create FHIR JSON
fhir_json = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": [{
        "fullUrl": f"Patient/{root.find('.//{http://www.gekid.de/namespace}Patient').attrib['Patient_ID']}",
        "resource": {
            "resourceType": "Patient",
            "id": root.find('.//{http://www.gekid.de/namespace}Patient').attrib['Patient_ID'],
            "meta": {
                "source": f"{root.find('.//{http://www.gekid.de/namespace}Absender').attrib['Absender_ID']}.{root.find('.//{http://www.gekid.de/namespace}Absender').attrib['Software_ID']}:obds-to-fhir:0.0.0-test",
                "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]
            },
            "identifier": [{
                "type": {
                    "coding": [
                        {"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "PSEUDED"},
                        {"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical record number"}
                    ]
                },
                "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id",
                "value": root.find('.//{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}KrankenversichertenNr').text
            }],
            "gender": "male" if root.find('.//{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_Geschlecht').text == "M" else "female",
            "birthDate": f"{root.find('.//{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_Geburtsdatum').text[-5:-3]}-{root.find('.//{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_Geburtsdatum').text[3:5]}"
        },
        "request": {
            "method": "PUT",
            "url": f"Patient/{root.find('.//{http://www.gekid.de/namespace}Patient').attrib['Patient_ID']}"
        }
    }]
}

# Print the FHIR JSON
print(json.dumps(fhir_json, indent=4))
```
Make sure to save the input XML file as 'input.xml' in the same directory as the Python script. Also, adjust the code as needed to handle other elements and attributes in the XML file.