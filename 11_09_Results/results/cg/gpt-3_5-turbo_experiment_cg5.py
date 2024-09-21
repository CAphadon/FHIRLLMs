
import xml.etree.ElementTree as ET
import json

# Parse the xml file
tree = ET.parse('input.xml')
root = tree.getroot()

# Create a dictionary to store the FHIR json data
fhir_data = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": []
}

# Extract patient data from the xml
patient_data = {}
for patient in root.findall('.//{http://www.gekid.de/namespace}Patient'):
    patient_data["resourceType"] = "Patient"
    patient_data["id"] = patient.find('.//{http://www.gekid.de/namespace}Patient_ID').attrib.get('Patient_ID')
    patient_data["identifier"] = [{
        "system": "http://www.gekid.de/namespace",
        "value": patient.find('.//{http://www.gekid.de/namespace}KrankenversichertenNr').text
    }]
    patient_data["name"] = [{
        "family": patient.find('.//{http://www.gekid.de/namespace}Patienten_Nachname').text,
        "given": [patient.find('.//{http://www.gekid.de/namespace}Patienten_Vornamen').text]
    }]
    patient_data["gender"] = patient.find('.//{http://www.gekid.de/namespace}Patienten_Geschlecht').text
    patient_data["birthDate"] = patient.find('.//{http://www.gekid.de/namespace}Patienten_Geburtsdatum').text

# Add the patient data to the FHIR json
fhir_data["entry"].append({
    "resource": patient_data
})

# Convert the FHIR json to a string and print it
fhir_json = json.dumps(fhir_data, indent=4)
print(fhir_json)