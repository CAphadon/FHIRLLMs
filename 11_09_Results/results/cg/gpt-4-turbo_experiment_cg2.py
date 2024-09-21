import xml.etree.ElementTree as ET
import json
import hashlib

def hash_id(patient_id):
    return hashlib.sha256(patient_id.encode()).hexdigest()

def parse_xml_to_fhir(xml_content):
    root = ET.fromstring(xml_content)
    
    entries = []
    
    for patient in root.findall(".//{http://www.gekid.de/namespace}Patient"):
        patient_data = patient.find(".//{http://www.gekid.de/namespace}Patienten_Stammdaten")
        patient_id = patient_data.attrib['Patient_ID']
        hashed_id = hash_id(patient_id)
        full_url = f"Patient/{hashed_id}"
        
        absender = root.find(".//{http://www.gekid.de/namespace}Absender")
        absender_id = absender.attrib['Absender_ID']
        software_id = absender.attrib['Software_ID']
        installation_id = absender.attrib['Installations_ID']
        meta_source = f"{absender_id}.{software_id}:{installation_id}-test"
        
        patient_gender = patient_data.find(".//{http://www.gekid.de/namespace}Patienten_Geschlecht").text
        gender = "male" if patient_gender == "M" else "female"
        
        birth_date = patient_data.find(".//{http://www.gekid.de/namespace}Patienten_Geburtsdatum").text
        birth_date = "-".join(reversed(birth_date.split(".")))
        
        address = patient_data.find(".//{http://www.gekid.de/namespace}Adresse")
        postal_code = address.find(".//{http://www.gekid.de/namespace}Patienten_PLZ").text
        country = address.find(".//{http://www.gekid.de/namespace}Patienten_Land").text
        
        entry = {
            "fullUrl": full_url,
            "resource": {
                "resourceType": "Patient",
                "id": hashed_id,
                "meta": {
                    "source": meta_source,
                    "profile": [
                        "https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"
                    ]
                },
                "identifier": [{
                    "type": {
                        "coding": [
                            {"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "PSEUDED"},
                            {"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical record number"}
                        ]
                    },
                    "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id",
                    "value": patient_id
                }],
                "gender": gender,
                "birthDate": birth_date[:7],  # Only year and month
                "address": [{
                    "type": "both",
                    "postalCode": postal_code,
                    "country": country
                }]
            },
            "request": {
                "method": "PUT",
                "url": full_url
            }
        }
        
        entries.append(entry)
    
    fhir_bundle = {
        "resourceType": "Bundle",
        "type": "transaction",
        "entry": entries
    }
    
    return json.dumps(fhir_bundle, indent=4)

# Example XML content
xml_content = '''
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
'''

fhir_json = parse_xml_to_fhir(xml_content)
print(fhir_json)
