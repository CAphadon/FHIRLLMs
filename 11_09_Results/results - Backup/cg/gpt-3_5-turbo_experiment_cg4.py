import xml.etree.ElementTree as ET
import json

# Parse the XML file
tree = ET.parse('input.xml')
root = tree.getroot()

# Create the FHIR Bundle JSON
fhir_json = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": [
        {
            "resource": {
                "resourceType": "Patient",
                "id": root.find('.//{http://www.gekid.de/namespace}Patienten_Stammdaten').get('Patient_ID'),
                "identifier": [
                    {
                        "system": "http://www.gekid.de/namespace",
                        "value": root.find('.//{http://www.gekid.de/namespace}KrankenversichertenNr').text
                    }
                ],
                "name": [
                    {
                        "family": root.find('.//{http://www.gekid.de/namespace}Patienten_Nachname').text,
                        "given": [root.find('.//{http://www.gekid.de/namespace}Patienten_Vornamen').text]
                    }
                ],
                "gender": root.find('.//{http://www.gekid.de/namespace}Patienten_Geschlecht').text,
                "birthDate": root.find('.//{http://www.gekid.de/namespace}Patienten_Geburtsdatum').text,
                "address": [
                    {
                        "line": [root.find('.//{http://www.gekid.de/namespace}Patienten_Strasse').text],
                        "postalCode": root.find('.//{http://www.gekid.de/namespace}Patienten_PLZ').text,
                        "city": root.find('.//{http://www.gekid.de/namespace}Patienten_Ort').text,
                        "country": root.find('.//{http://www.gekid.de/namespace}Patienten_Land').text
                    }
                ]
            }
        }
    ]
}

# Print the FHIR JSON
print(json.dumps(fhir_json, indent=2))