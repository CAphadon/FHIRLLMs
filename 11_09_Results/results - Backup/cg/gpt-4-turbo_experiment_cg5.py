To create a Python program that converts the XML content described to a FHIR JSON format, we can use libraries such as `xml.etree.ElementTree` for parsing XML and `json` for constructing and displaying the JSON structure. Below is the runnable Python code that fulfills the requirements. Note that the XML data provided in the question is used as a string within the script for demonstration purposes.

```python
import xml.etree.ElementTree as ET
import json

# Sample XML data as a string
xml_data = """
<ns0:ADT_GEKID xmlns:ns0="http://www.gekid.de/namespace" Schema_Version="2.2.1">
    <ns0:Absender Absender_ID="22222244" Software_ID="ONKOSTAR" Installations_ID="2.9.8">
        <ns0:Absender_Bezeichnung>UKER</ns0:Absender_Bezeichnung>
        <ns0:Absender_Ansprechpartner />
        <ns0:Absender_Anschrift>Maximiliansplatz 2, 91054 Erlangen</ns0:Absender_Anschrift>
    </ns0:Absender>
    <ns0:Menge_Patient>
        <ns0:Patient>
            <ns0:Patienten_Stammdaten Patient_ID="123456789">
                <ns0:KrankenversichertenNr>Q123456</ns0:KrankenversichertenNr>
                <ns0:KrankenkassenNr>555555</ns0:KrankenkassenNr>
                <ns0:Patienten_Nachname>Max</ns0:Patienten_Nachname>
                <ns0:Patienten_Vornamen>Mustermann</ns0:Patienten_Vornamen>
                <ns0:Patienten_Geschlecht>M</ns0:Patienten_Geschlecht>
                <ns0:Patienten_Geburtsdatum>02.04.2023</ns0:Patienten_Geburtsdatum>
                <ns0:Menge_Adresse>
                    <ns0:Adresse>
                        <ns0:Patienten_Strasse>Bahnhofstr. 1</ns0:Patienten_Strasse>
                        <ns0:Patienten_Land>DE</ns0:Patienten_Land>
                        <ns0:Patienten_PLZ>70070</ns0:Patienten_PLZ>
                        <ns0:Patienten_Ort>Tuebingen</ns0:Patienten_Ort>
                    </ns0:Adresse>
                </ns0:Menge_Adresse>
            </ns0:Patienten_Stammdaten>
        </ns0:Patient>
    </ns0:Menge_Patient>
</ns0:ADT_GEKID>
"""

# Parse XML from the string
root = ET.fromstring(xml_data)

# Namespace handling
ns = {'ns0': 'http://www.gekid.de/namespace'}

# Extract data from XML
patient_data = root.find('.//ns0:Patienten_Stammdaten', ns)
addresses = patient_data.find('.//ns0:Menge_Adresse', ns)

# Constructing the FHIR JSON
fhir_json = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": [{
        "resource": {
            "resourceType": "Patient",
            "id": patient_data.get('Patient_ID'),
            "identifier": [
                {"use": "official", "value": patient_data.find('ns0:KrankenversichertenNr', ns).text},
                {"use": "secondary", "value": patient_data.find('ns0:KrankenkassenNr', ns).text}
            ],
            "name": [{
                "family": patient_data.find('ns0:Patienten_Nachname', ns).text,
                "given": [patient_data.find('ns0:Patienten_Vornamen', ns).text],
            }],
            "gender": "male" if patient_data.find('ns0:Patienten_Geschlecht', ns).text == 'M' else "female",
            "birthDate": patient_data.find('ns0:Patienten_Geburtsdatum', ns).text.replace('.', '-'),
            "address": [{
                "use": "home",
                "line": [addresses.find('.//ns0:Patienten_Strasse', ns).text],
                "city": addresses.find('.//ns0:Patienten_Ort', ns).text,
                "postalCode": addresses.find('.//ns0:Patienten_PLZ', ns).text,
                "country": addresses.find('.//ns0:Patienten_Land', ns).text
            }]
        }
    }]
}

# Print the resulting FHIR JSON
print(json.dumps(fhir_json, indent=4))
```

This code snippet does the following:
- Parses the sample XML.
- Extracts relevant patient information.
- Constructs a FHIR JSON Bundle of type 'transaction' with a single 'Patient' entry containing details extracted from the XML.
- Prints the JSON output.

For a real-world application, you would typically read the XML from a file or another source, handle more complex cases, and possibly deal with multiple entries. Additionally, for more advanced XML parsing or more complex XML structures, you might consider using `lxml` instead of `xml.etree.ElementTree`.