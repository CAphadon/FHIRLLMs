import xml.etree.ElementTree as ET
import json
import hashlib

def parse_xml_to_fhir(xml_content):
    # Parse XML content
    root = ET.fromstring(xml_content)
    
    # Namespace map
    ns = {'ns0': 'http://www.gekid.de/namespace'}

    # Extract sender information
    sender = root.find('ns0:Absender', ns)
    sender_id = sender.get('Absender_ID')
    software_id = sender.get('Software_ID')

    # Extract patient information
    patient = root.find('.//ns0:Patient/ns0:Patienten_Stammdaten', ns)
    patient_id = patient.get('Patient_ID')
    gender = patient.find('ns0:Patienten_Geschlecht', ns).text
    birthdate = patient.find('ns0:Patienten_Geburtsdatum', ns).text
    birthdate_fhir_format = "{}-{}".format(birthdate.split('.')[2], birthdate.split('.')[1])  # Convert to YYYY-MM

    # Generate a stable unique ID based on patient ID
    hash_object = hashlib.sha256(patient_id.encode())
    patient_uuid = hash_object.hexdigest()

    # Create a FHIR JSON structure
    fhir_json = {
        "resourceType": "Bundle",
        "type": "transaction",
        "entry": [
            {
                "fullUrl": f"Patient/{patient_uuid}",
                "resource": {
                    "resourceType": "Patient",
                    "id": patient_uuid,
                    "meta": {
                        "source": f"{sender_id}.{software_id}:obds-to-fhir:0.0.0-test",
                        "profile": [
                            "https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"
                        ]
                    },
                    "identifier": [
                        {
                            "type": {
                                "coding": [
                                    {"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "PSEUDED"},
                                    {"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical record number"}
                                ]
                            },
                            "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id",
                            "value": patient_id
                        }
                    ],
                    "gender": "male" if gender == 'M' else "female",
                    "birthDate": birthdate_fhir_format,
                    "address": [
                        {
                            "type": "both",
                            "postalCode": patient.find('.//ns0:Patienten_PLZ', ns).text,
                            "country": patient.find('.//ns0:Patienten_Land', ns).text
                        }
                    ]
                },
                "request": {
                    "method": "PUT",
                    "url": f"Patient/{patient_uuid}"
                }
            }
        ]
    }

    return fhir_json

# Sample XML input
xml_input = '''
<ns0:ADT_GEKID xmlns:ns0="http://www.gekid.de/namespace" Schema_Version="2.2.1">
    <ns0:Absender Absender_ID="999999" Software_ID="ONKOSTAR" Installations_ID="2.9.8">
        <ns0:Absender_Bezeichnung>UKER</ns0:Absender_Bezeichnung>
        <ns0:Absender_Anschrift>Maximiliansplatz 2, 91054 Erlangen</ns0:Absender_Anschrift>
    </ns0:Absender>
    <ns0:Menge_Patient>
        <ns0:Patient>
            <ns0:Patienten_Stammdaten Patient_ID="1055555888">
                <ns0:KrankenversichertenNr>Q00000000</ns0:KrankenversichertenNr>
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
</ns0:ADT_GEKID>
'''

# Parse and print FHIR JSON
fhir_json_output = parse_xml_to_fhir(xml_input)
print(json.dumps(fhir_json_output, indent=4))
