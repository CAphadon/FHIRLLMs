To convert the given XML data into an FHIR JSON of resourceType 'Bundle' with type 'transaction' and a 'Patient' entry, we'll use Python with the `xml.etree.ElementTree` library for parsing the XML and the `json` library to create the JSON output. Below is the runnable Python code that performs this transformation and prints the resulting FHIR JSON to the console:

```python
import xml.etree.ElementTree as ET
import json

def parse_patient_data(xml_element):
    patient_data = {}

    patient_data['resourceType'] = 'Patient'
    patient_data['id'] = xml_element.find('{http://www.gekid.de/namespace}Patienten_Stammdaten').get('Patient_ID')
    patient_data['identifier'] = [
        {
            'system': 'urn:oid:1.2.276.0.76.3.1',
            'value': xml_element.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}KrankenversichertenNr').text
        }
    ]
    patient_data['name'] = [
        {
            'family': xml_element.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_Nachname').text,
            'given': [xml_element.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_Vornamen').text]
        }
    ]
    patient_data['gender'] = 'male' if xml_element.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_Geschlecht').text == 'M' else 'female'
    patient_data['birthDate'] = xml_element.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_Geburtsdatum').text

    address_element = xml_element.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Menge_Adresse/{http://www.gekid.de/namespace}Adresse')
    patient_data['address'] = [
        {
            'line': [address_element.find('{http://www.gekid.de/namespace}Patienten_Strasse').text],
            'city': address_element.find('{http://www.gekid.de/namespace}Patienten_Ort').text,
            'postalCode': address_element.find('{http://www.gekid.de/namespace}Patienten_PLZ').text,
            'country': address_element.find('{http://www.gekid.de/namespace}Patienten_Land').text
        }
    ]

    return patient_data

def xml_to_fhir_json(xml_string):
    root = ET.fromstring(xml_string)

    # Extract Patient Data
    patient_element = root.find('{http://www.gekid.de/namespace}Menge_Patient/{http://www.gekid.de/namespace}Patient')
    patient_data = parse_patient_data(patient_element)
    
    # Create the FHIR Bundle
    fhir_bundle = {
        'resourceType': 'Bundle',
        'type': 'transaction',
        'entry': [
            {
                'resource': patient_data
            }
        ]
    }

    return json.dumps(fhir_bundle, indent=2)

xml_input = '''<ns0:ADT_GEKID xmlns:ns0="http://www.gekid.de/namespace" Schema_Version="2.2.1">
    <ns0:Absender Absender_ID="22222244" Software_ID="ONKOSTAR" Installations_ID="2.9.8">
        <ns0:Absender_Bezeichnung>UKER</ns0:Absender_Bezeichnung>
        <ns0:Absender_Ansprechpartner />
        <ns0:Absender_Anschrift>Maximiliansplatz 2, 91054 Erlangen</ns0:Absender_Anschrift>
    </ns0:Absender>
    <ns0:Menge_Patient>
        <ns0:Patient>
            <ns0:Patienten_Stammdaten Patient_ID="123456789">
                <ns0:KrankenversichertenNr>Q123456</ns0:KrankenversichertenNr>
                <ns0:KrankenkassenNr>555555</ns0:KrankenkassenNr>
                <ns0:Patienten_Nachname>Max</ns0:Patienten_Nachname>
                <ns0:Patienten_Vornamen>Mustermann</ns0:Patienten_Vornamen>
                <ns0:Patienten_Geschlecht>M</ns0:Patienten_Geschlecht>
                <ns0:Patienten_Geburtsdatum>02.04.2023</ns0:Patienten_Geburtsdatum>
                <ns0:Menge_Adresse>
                    <ns0:Adresse>
                        <ns0:Patienten_Strasse>Bahnhofstr. 1</ns0:Patienten_Strasse>
                        <ns0:Patienten_Land>DE</ns0:Patienten_Land>
                        <ns0:Patienten_PLZ>70070</ns0:Patienten_PLZ>
                        <ns0:Patienten_Ort>Tuebingen</ns0:Patienten_Ort>
                    </ns0:Adresse>
                </ns0:Menge_Adresse>
            </ns0:Patienten_Stammdaten>
        </ns0:Patient>
    </ns0:Menge_Patient>
    <ns0:Menge_Melder>
        <ns0:Melder Melder_ID="ST">
            <ns0:Meldende_Stelle>ST</ns0:Meldende_Stelle>
        </ns0:Melder>
    </ns0:Menge_Melder>
</ns0:ADT_GEKID>'''

fhir_json = xml_to_fhir_json(xml_input)
print(fhir_json)
```

This code will parse the given XML, extract the necessary patient information, and convert it into the FHIR JSON format, then print the resulting JSON to the console. The resulting FHIR JSON will be formatted as a 'Bundle' containing a 'Patient' entry.