 

The expected output should look like this:

```
{
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": [
        {
            "resource": {
                "resourceType": "Patient",
                "id": "123456789",
                "identifier": [
                    {
                        "value": "Q123456"
                    }
                ],
                "name": [
                    {
                        "given": [
                            "Mustermann"
                        ],
                        "family": "Max"
                    }
                ],
                "gender": "male",
                "birthDate": "2023-04-02",
                "address": [
                    {
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
```

Note: The gender value in the output should be'male' instead of 'M'. 