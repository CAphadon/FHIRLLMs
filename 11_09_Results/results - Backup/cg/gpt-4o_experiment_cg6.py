Certainly! Below is a runnable Python code snippet that reads the XML data, processes it, and prints the resulting FHIR JSON:

```python
import xml.etree.ElementTree as ET
import json
import hashlib

# Sample XML input
xml_data = '''<ns0:ADT_GEKID xmlns:ns0="http://www.gekid.de/namespace" Schema_Version="2.2.1">
    <ns0:Absender Absender_ID="999999" Software_ID="ONKOSTAR" Installations_ID="2.9.8">
        <ns0:Absender_Bezeichnung>UKER</ns0:Absender_Bezeichnung>
        <ns0:Absender_Ansprechpartner />
        <ns0:Absender_Anschrift>Maximiliansplatz 2, 91054 Erlangen</ns0:Absender_Anschrift>
    </ns0:Absender>
    <ns0:Menge_Patient>
        <ns0:Patient>
            <ns0:Patienten_Stammdaten Patient_ID="1055555888">
                <ns0:KrankenversichertenNr>Q00000000</ns0:KrankenversichertenNr>
                <ns0:KrankenkassenNr>10000000</ns0:KrankenkassenNr>
                <ns0:Patienten_Nachname>Doe</ns0:Patienten_Nachname>
                <ns0:Patienten_Vornamen>John</ns0:Patienten_Vornamen>
                <ns0:Patienten_Geschlecht>M</ns0:Patienten_Geschlecht>
                <ns0:Patienten_Geburtsdatum>11.09.1900</ns0:Patienten_Geburtsdatum>
                <ns0:Menge_Adresse>
                    <ns0:Adresse>
                        <ns0:Patienten_Strasse>Johnstr. 7</ns0:Patienten_Strasse>
                        <ns0:Patienten_Land>DE</ns0:Patienten_Land>
                        <ns0:Patienten_PLZ>91000</ns0:Patienten_PLZ>
                        <ns0:Patienten_Ort>Johncity</ns0:Patienten_Ort>
                    </ns0:Adresse>
                </ns0:Menge_Adresse>
            </ns0:Patienten_Stammdaten>
        </ns0:Patient>
    </ns0:Menge_Patient>
</ns0:ADT_GEKID>'''

def parse_xml_to_json(xml_string):
    # Parse the XML string
    root = ET.fromstring(xml_string)
    ns = {'ns0': 'http://www.gekid.de/namespace'}
    
    # Extract the patient data
    patient_node = root.find('.//ns0:Patient', ns)
    patient_id = patient_node.find('.//ns0:Patienten_Stammdaten', ns).attrib['Patient_ID']
    gender = patient_node.find('.//ns0:Patienten_Geschlecht', ns).text
    birthdate = patient_node.find('.//ns0:Patienten_Geburtsdatum', ns).text
    postal_code = patient_node.find('.//ns0:Patienten_PLZ', ns).text
    country = patient_node.find('.//ns0:Patienten_Land', ns).text

    # Convert birthdate to FHIR format (YYYY-MM)
    birthdate_parts = birthdate.split('.')
    birthdate_fhir = f'{birthdate_parts[2]}-{birthdate_parts[1]}'

    # Convert gender to FHIR format
    gender_fhir = 'male' if gender == 'M' else 'female'

    # Create a hash for the patient ID to use as resource ID
    resource_id = hashlib.sha256(patient_id.encode()).hexdigest()

    # Build the JSON structure
    fhir_json = {
        "resourceType": "Bundle",
        "type": "transaction",
        "entry": [{
            "fullUrl": f"Patient/{resource_id}",
            "resource": {
                "resourceType": "Patient",
                "id": resource_id,
                "meta": {
                    "source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test",
                    "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]
                },
                "identifier": [{
                    "type": {
                        "coding": [
                            {"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "PSEUDED"},
                            {"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical·record·number"}
                        ]
                    },
                    "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id",
                    "value": patient_id
                }],
                "gender": gender_fhir,
                "birthDate": birthdate_fhir,
                "address": [{
                    "type": "both",
                    "postalCode": postal_code,
                    "country": country
                }]
            },
            "request": {
                "method": "PUT",
                "url": f"Patient/{resource_id}"
            }
        }]
    }

    return fhir_json

# Parse the XML and convert to JSON
fhir_json = parse_xml_to_json(xml_data)

# Print the resulting JSON to the console
print(json.dumps(fhir_json, indent=4))
```

This script processes the provided XML data and converts it into the desired FHIR JSON format. The `parse_xml_to_json` function extracts the necessary information from the XML, processes it, and constructs the FHIR JSON structure. Finally, the JSON is printed to the console with indentation for readability.