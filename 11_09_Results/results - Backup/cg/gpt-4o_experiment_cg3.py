```python
import xml.etree.ElementTree as ET
import hashlib
import json

# Function to hash any input string
def generate_hash(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()

def xml_to_fhir(xml_data):
    # Parse the XML data
    root = ET.fromstring(xml_data)
    ns = {'ns0': 'http://www.gekid.de/namespace'}
    
    # Extract Patient Information
    patient = root.find('.//ns0:Patient', ns)
    patient_id = patient.find('.//ns0:Patienten_Stammdaten', ns).get('Patient_ID')
    gender = patient.find('.//ns0:Patienten_Geschlecht', ns).text
    birth_date = patient.find('.//ns0:Patienten_Geburtsdatum', ns).text
    postal_code = patient.find('.//ns0:Patienten_PLZ', ns).text
    country = patient.find('.//ns0:Patienten_Land', ns).text

    # Map gender to FHIR standard
    gender_map = {'M': 'male', 'F': 'female'}
    gender = gender_map.get(gender, 'unknown')

    # Convert date format from dd.mm.yyyy to yyyy-mm
    birth_date_parts = birth_date.split('.')
    birth_date_fhir = f"{birth_date_parts[2]}-{birth_date_parts[1]}"

    # Generate the patient hash
    patient_hash = generate_hash(patient_id)

    # Construct FHIR Resource JSON
    fhir_resource = {
        "resourceType": "Bundle",
        "type": "transaction",
        "entry": [
            {
                "fullUrl": f"Patient/{patient_hash}",
                "resource": {
                    "resourceType": "Patient",
                    "id": patient_hash,
                    "meta": {
                        "source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test",
                        "profile": [
                            "https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"
                        ]
                    },
                    "identifier": [
                        {
                            "type": {
                                "coding": [
                                    {
                                        "system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue",
                                        "code": "PSEUDED"
                                    },
                                    {
                                        "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                        "code": "MR",
                                        "display": "Medical·record·number"
                                    }
                                ]
                            },
                            "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id",
                            "value": patient_id
                        }
                    ],
                    "gender": gender,
                    "birthDate": birth_date_fhir,
                    "address": [
                        {
                            "type": "both",
                            "postalCode": postal_code,
                            "country": country
                        }
                    ]
                },
                "request": {
                    "method": "PUT",
                    "url": f"Patient/{patient_hash}"
                }
            }
        ]
    }

    # Print the resulting FHIR JSON
    print(json.dumps(fhir_resource, indent=2))

# Test Data
xml_data = """<ns0:ADT_GEKID xmlns:ns0="http://www.gekid.de/namespace" Schema_Version="2.2.1">
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
</ns0:ADT_GEKID>"""

# Convert XML to FHIR JSON and print it
xml_to_fhir(xml_data)
```