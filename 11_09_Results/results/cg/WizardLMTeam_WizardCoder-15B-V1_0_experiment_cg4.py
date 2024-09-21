Do not include any external libraries that can make the code more complex. 

The resulting FHIR json should be:

{
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": [
        {
            "fullUrl": "urn:uuid:123456789",
            "resource": {
                "resourceType": "Patient",
                "id": "123456789",
                "name": [
                    {
                        "use": "official",
                        "family": "Max",
                        "given": [
                            "Mustermann"
                        ]
                    }
                ],
                "gender": "male",
                "birthDate": "2023-04-02",
                "address": [
                    {
                        "use": "home",
                        "line": [
                            "Bahnhofstr. 1"
                        ],
                        "city": "Tuebingen",
                        "postalCode": "70070",
                        "country": "DE"
                    }
                ]
            }
        }
    ]
}