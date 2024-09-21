import xml.etree.ElementTree as ET
import hashlib
import json

def parse_xml_to_fhir(xml_data):
    # Parse XML data
    ns = {'ns0': 'http://www.gekid.de/namespace'}
    root = ET.fromstring(xml_data)
    
    # Get the sender information
    sender = root.find('ns0:Absender', ns)
    sender_id = sender.get('Absender_ID')
    software_id = sender.get('Software_ID')
    
    # Create FHIR bundle
    fhir_bundle = {
        "resourceType": "Bundle",
        "type": "transaction",
        "entry": []
    }

    # Process each patient
    for patient in root.findall('ns0:Menge_Patient/ns0:Patient', ns):
        patient_data = patient.find('ns0:Patienten_Stammdaten', ns)
        patient_id = patient_data.get('Patient_ID')
        patient_gender = patient_data.find('ns0:Patienten_Geschlecht', ns).text
        patient_birthdate = patient_data.find('ns0:Patienten_Geburtsdatum', ns).text
        patient_address = patient_data.find('ns0:Menge_Adresse/ns0:Adresse', ns)
        patient_postal_code = patient_address.find('ns0:Patienten_PLZ', ns).text
        patient_country = patient_address.find('ns0:Patienten_Land', ns).text
        
        # Hash the patient ID to generate a unique identifier
        hash_object = hashlib.sha1(patient_id.encode())
        patient_hash_id = hash_object.hexdigest()

        # Map gender to FHIR standard
        gender_map = {'M': 'male', 'F': 'female', 'U': 'unknown'}
        fhir_gender = gender_map.get(patient_gender, 'unknown')

        # Convert birthdate to FHIR format
        day, month, year = patient_birthdate.split('.')
        fhir_birthdate = f"{year}-{month}"

        # Build the patient resource
        patient_resource = {
            "resourceType": "Patient",
            "id": patient_hash_id,
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
            "gender": fhir_gender,
            "birthDate": fhir_birthdate,
            "address": [
                {
                    "type": "both",
                    "postalCode": patient_postal_code,
                    "country": patient_country
                }
            ]
        }

        # Add to bundle
        fhir_bundle['entry'].append({
            "fullUrl": f"Patient/{patient_hash_id}",
            "resource": patient_resource,
            "request": {
                "method": "PUT",
                "url": f"Patient/{patient_hash_id}"
            }
        })

    # Print FHIR JSON output
    print(json.dumps(fhir_bundle, indent=2))

# Example XML data
xml_data = """
<ns0:ADT_GEKID xmlns:ns0="http://www.gekid.de/namespace" Schema_Version="2.2.1">
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
</ns0:ADT_GEKID>
"""

# Run the conversion function
parse_xml_to_fhir(xml_data)