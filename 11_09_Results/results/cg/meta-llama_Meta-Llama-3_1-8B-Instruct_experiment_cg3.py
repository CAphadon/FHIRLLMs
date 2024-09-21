import xml.etree.ElementTree as ET
import json
import uuid
from datetime import datetime
from fhirpy import Client

# XML to JSON conversion
def xml_to_json(xml_string):
    root = ET.fromstring(xml_string)
    patients = root.findall('.//ns0:Menge_Patient/ns0:Patient')
    json_data = []
    for patient in patients:
        patient_id = patient.find('.//ns0:Patienten_Stammdaten/ns0:Patienten_ID').text
        json_data.append({
           'resourceType': 'Patient',
            'id': patient_id,
            'identifier': [
                {'type': {'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationValue', 'code': 'PSEUDED'}, {'system': 'http://terminology.hl7.org/CodeSystem/v2-0203', 'code': 'MR', 'display': 'Medical\u00b0record\u00b0number'}]},'system': 'https://fhir.diz.uk-erlangen.de/identifiers/patient-id', 'value': patient_id},
            ],
            'birthDate': datetime.strptime(patient.find('.//ns0:Patienten_Geburtsdatum').text, '%d.%m.%Y').strftime('%Y-%m-%d'),
            'gender': patient.find('.//ns0:Patienten_Geschlecht').text,
            'name': [
                {
                    'family': patient.find('.//ns0:Patienten_Nachname').text,
                    'given': [patient.find('.//ns0:Patienten_Vornamen').text],
                },
            ],
            'address': [
                {
                    'use': 'both',
                    'line': [patient.find('.//ns0:Patienten_Strasse').text],
                    'city': patient.find('.//ns0:Patienten_Ort').text,
                    'postalCode': patient.find('.//ns0:Patienten_PLZ').text,
                    'country': patient.find('.//ns0:Patienten_Land').text,
                },
            ],
        })
    return json_data

# Convert XML string to JSON
xml_string = '''<ns0:ADT_GEKID xmlns:ns0="http://www.gekid.de/namespace" Schema_Version="2.2.1">
    <!--... -->
</ns0:ADT_GEKID>'''

json_data = xml_to_json(xml_string)

# Convert JSON to FHIR Bundle
bundle = {
   'resourceType': 'Bundle',
    'type': 'transaction',
    'entry': [],
}
for patient in json_data:
    entry = {
        'fullUrl': f'Patient/{patient["id"]}',
       'resource': patient,
       'request': {
           'method': 'PUT',
            'url': f'Patient/{patient["id"]}',
        },
    }
    bundle['entry'].append(entry)

# Print FHIR Bundle to console
print(json.dumps(bundle, indent=4))

