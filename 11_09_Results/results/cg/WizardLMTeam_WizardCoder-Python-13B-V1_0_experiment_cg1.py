import json
from xml.etree import ElementTree as ET

# Read the xml file
xml_data = ET.parse('input.xml')

# Create a dictionary for the data
data = {}

# Get the Absender data
absender_data = {
    "sender": {
        "id": "999999",
        "software_id": "ONKOSTAR",
        "installation_id": "2.9.8",
        "name": xml_data.find(".//ns0:Absender_Bezeichnung", {'ns0': 'http://www.gekid.de/namespace'}).text,
        "address": xml_data.find(".//ns0:Absender_Anschrift", {'ns0': 'http://www.gekid.de/namespace'}).text
    }
}

# Get the patient data
patient_data = {
    "id": xml_data.find(".//ns0:KrankenversichertenNr", {'ns0': 'http://www.gekid.de/namespace'}).text,
    "insurance": xml_data.find(".//ns0:KrankenkassenNr", {'ns0': 'http://www.gekid.de/namespace'}).text,
    "last_name": xml_data.find(".//ns0:Patienten_Nachname", {'ns0': 'http://www.gekid.de/namespace'}).text,
    "first_name": xml_data.find(".//ns0:Patienten_Vornamen", {'ns0': 'http://www.gekid.de/namespace'}).text,
    "gender": xml_data.find(".//ns0:Patienten_Geschlecht", {'ns0': 'http://www.gekid.de/namespace').text,
    "birth_date": xml_data.find(".//ns0:Patienten_Geburtsdatum", {'ns0': 'http://www.gekid.de/namespace').text,
    "address": {
        "street": xml_data.find(".//ns0:Patienten_Strasse", {'ns0': 'http://www.gekid.de/namespace').text,
        "country": xml_data.find(".//ns0:Patienten_Land", {'ns0': 'http://www.gekid.de/namespace').text,
        "zipcode": xml_data.find(".//ns0:Patienten_PLZ", {'ns0': 'http://www.gekid.de/namespace').text,
        "city": xml_data.find(".//ns0:Patienten_Ort", {'ns0': 'http://www.gekid.de/namespace').text
    }
}

# Get the ST data
st_data = {
    "id": xml_data.find(".//ns0:ST_ID", {'ns0': 'http://www.gekid.de/namespace').text,
    "intention": xml_data.find(".//ns0:ST_Intention", {'ns0': 'http://www.gekid.de/namespace').text,
    "op_position": xml_data.find(".//ns0:ST_Stellung_OP", {'ns0': 'http://www.gekid.de/namespace').text,
    "diagnose_code": xml_data.find(".//ns0:Primaertumor_ICD_Code", {'ns0': 'http://www.gekid.de/namespace').text,
    "diagnose_version": xml_data.find(".//ns0:Primaertumor_ICD_Version", {'ns0': 'http://www.gekid.de/namespace').text,
    "diagnose_date": xml_data.find(".//ns0:Diagnosedatum", {'ns0': 'http://www.gekid.de/namespace').text,
    "location": xml_data.find(".//ns0:Seitenlokalisation", {'ns0': 'http://www.gekid.de/namespace').text,
    "end_cause": xml_data.find(".//ns0:ST_Ende_Grund", {'ns0': 'http://www.gekid.de/namespace').text,
    "side": xml_data.find(".//ns0:ST_Seite_Zielgebiet", {'ns0': 'http://www.gekid.de/namespace').text,
    "end_date": xml_data.find(".//ns0:ST_Ende_Datum", {'ns0': 'http://www.gekid.de/namespace').text,
    "grade": xml_data.find(".//ns0:Nebenwirkung_Grad", {'ns0': 'http://www.gekid.de/namespace').text
}

# Add the data to the dictionary
data["absender"] = absender_data
data["patient"] = patient_data
data["st"] = st_data

# Create the FHIR Json
fhir_json = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": [
        {
            "fullUrl": "Patient/" + patient_data["id"],
            "resource": {
                "resourceType": "Patient",
                "id": patient_data["id"],
                "meta": {
                    "source": f"{absender_data['id']}.{absender_data['software_id']}:obds-to-fhir:0.0.0-test",
                    "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]
                },
                "identifier": [{
                    "type": {
                        "coding": [
                            {"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "PSEUDED"},
                            {"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical\u00b7record\u00b7number"}
                        ],
                        "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id",
                        "value": patient_data["id"]
                    }
                }],
                "gender": patient_data["gender"],
                "birthDate": patient_data["birth_date"],
                "address": [
                    {
                        "type": "both",
                        "postalCode": patient_data["address"]["zipcode"],
                        "country": patient_data["address"]["country"]
                    }
                ]
            },
            "request": {
                "method": "PUT",
                "url": f"Patient/{patient_data['id']}"
            }
        }
    ]
}

# Print the FHIR json
print(json.dumps(fhir_json))