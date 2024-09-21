import xml.etree.ElementTree as ET
import json

def parse_patient(patient):
    patient_id = patient.find('ns0:Patienten_Stammdaten', ns).get('Patient_ID')
    gender = patient.find('ns0:Patienten_Stammdaten/ns0:Patienten_Geschlecht', ns).text
    birth_date = patient.find('ns0:Patienten_Stammdaten/ns0:Patienten_Geburtsdatum', ns).text
    postal_code = patient.find('ns0:Patienten_Stammdaten/ns0:Menge_Adresse/ns0:Adresse/ns0:Patienten_PLZ', ns).text
    country = patient.find('ns0:Patienten_Stammdaten/ns0:Menge_Adresse/ns0:Adresse/ns0:Patienten_Land', ns).text
    return {
        'resourceType': 'Patient',
        'id': patient_id,
        'gender': 'male' if gender == 'M' else 'female',
        'birthDate': birth_date,
        'address': [{'type': 'both', 'postalCode': postal_code, 'country': country}]
    }

# Parse XML
ns = {'ns0': 'http://www.gekid.de/namespace'}
tree = ET.parse('input.xml')
root = tree.getroot()

# Get sender data
sender_data = root.find('ns0:Absender', ns)
sender_id = sender_data.get('Absender_ID')

# Get patient data
patients_data = root.findall('ns0:Menge_Patient/ns0:Patient', ns)
patients = [parse_patient(patient) for patient in patients_data]

# Create JSON
output = {
    'resourceType': 'Bundle',
    'type': 'transaction',
    'entry': [
        {
            'fullUrl': f'Patient/{patient["id"]}',
            'resource': patient,
            'request': {
                'method': 'PUT',
                'url': f'Patient/{patient["id"]}'
            }
        } for patient in patients
    ]
}

# Print JSON
print(json.dumps(output, indent=4))
