Sure, here is a Python code snippet to perform the task:

```python
import json
import xml.etree.ElementTree as ET

def xml_to_json(xml_string):
    tree = ET.ElementTree(ET.fromstring(xml_string))
    root = tree.getroot()

    patient_data = root.find('{http://www.gekid.de/namespace}Menge_Patient').find('{http://www.gekid.de/namespace}Patient').find('{http://www.gekid.de/namespace}Patienten_Stammdaten')
    patient_address = patient_data.find('{http://www.gekid.de/namespace}Menge_Adresse').find('{http://www.gekid.de/namespace}Adresse')

    patient_json = {
        'resourceType': 'Patient',
        'id': patient_data.attrib['Patient_ID'],
        'name': [{
            'family': patient_data.find('{http://www.gekid.de/namespace}Patienten_Nachname').text,
            'given':[patient_data.find('{http://www.gekid.de/namespace}Patienten_Vornamen').text]
        }],
        'gender': 'male' if patient_data.find('{http://www.gekid.de/namespace}Patienten_Geschlecht').text == 'M' else 'female',
        'birthDate': patient_data.find('{http://www.gekid.de/namespace}Patienten_Geburtsdatum').text,
        'address': [{
            'line': [patient_address.find('{http://www.gekid.de/namespace}Patienten_Strasse').text],
            'city': patient_address.find('{http://www.gekid.de/namespace}Patienten_Ort').text,
            'postalCode': patient_address.find('{http://www.gekid.de/namespace}Patienten_PLZ').text,
            'country': patient_address.find('{http://www.gekid.de/namespace}Patienten_Land').text
        }]
    }

    fhir_json = {
        'resourceType': 'Bundle',
        'type': 'transaction',
        'entry': [{'resource': patient_json}]
    }

    return json.dumps(fhir_json, indent=4)

# Replace the 'xml_string' variable with your XML file content
xml_string = '''
<ns0:ADT_GEKID xmlns:ns0="http://www.gekid.de/namespace" Schema_Version="2.2.1">
...
</ns0:ADT_GEKID>
'''

print(xml_to_json(xml_string))
```

Please note that you need to replace the 'xml_string' variable with the content of your XML file. Also, this code assumes that the XML structure is always the same as the one you've provided and the presence of all XML elements is guaranteed. If it's not the case, you might want to add some error handling or checks for the existence of the XML elements before accessing them.