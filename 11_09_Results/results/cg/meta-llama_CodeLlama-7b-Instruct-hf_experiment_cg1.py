import xml.etree.ElementTree as ET
import json

def main():
    xml = ET.parse("ADT_GEKID.xml").getroot()
    patient_id = xml.find('ns0:Patienten_Stammdaten', ns0="http://www.gekid.de/namespace").attrib['Patient_ID']
    json_ = {
        "resourceType": "Patient",
        "id": patient_id,
        "meta": {
            "source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test",
            "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]
        },
        "identifier": [{
            "type": {
                "coding": [{
                    "system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue",
                    "code": "PSEUDED"
                }, {
                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                    "code": "MR",
                    "display": "Medical\u00b7record\u00b7number"
                }]
            },
            "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id",
            "value": patient_id
        }],
        "gender": "male",
        "birthDate": "1900-07",
        "address": [
            {
                "type": "both",
                "postalCode": "91000",
                "country": "DE"
            }
        ]
    }
    return json.dumps(json_)

if __name__ == "__main__":
    print(main())
