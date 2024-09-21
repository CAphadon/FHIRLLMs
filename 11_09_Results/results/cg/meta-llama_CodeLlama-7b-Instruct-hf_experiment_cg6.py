import xml.etree.ElementTree as ET
from typing import Dict
import json

def main(xml_filename: str) -> str:
    tree = ET.parse(xml_filename)
    root = tree.getroot()
    # TODO
    result = {"resourceType": "Bundle", "type": "transaction", "entry": []}
    for patient in root.findall('.//ns0:Patient', namespaces={'ns0': 'http://www.gekid.de/namespace'}):
        patient_id = patient.attrib['Patient_ID']
        patient_resource = {
            "resourceType": "Patient",
            "id": f"d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937",
            "meta": {
                "source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test",
                "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]
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
                                "display": "Medical\u00b7record\u00b7number"
                            }
                        ]
                    },
                    "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id",
                    "value": patient_id
                }
            ],
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
        result["entry"].append({
            "fullUrl": f"Patient/d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937",
            "resource": patient_resource,
            "request": {
                "method": "PUT",
                "url": f"Patient/d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937"
            }
        })
    return json.dumps(result, indent=4, sort_keys=True)

if __name__ == '__main__':
    print(main('input.xml'))
