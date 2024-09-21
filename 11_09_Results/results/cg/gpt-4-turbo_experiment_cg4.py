import xml.etree.ElementTree as ET
import json

# Sample XML data as a multiline string
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

# Parse the XML data
root = ET.fromstring(xml_data)

# Define XML namespace
ns = {'ns0': 'http://www.gekid.de/namespace'}

# Extract patient data
patient_data = root.find('.//ns0:Patienten_Stammdaten', ns)
patient_name = patient_data.find('ns0:Patienten_Nachname', ns).text
patient_first_name = patient_data.find('ns0:Patienten_Vornamen', ns).text
patient_gender = patient_data.find('ns0:Patienten_Geschlecht', ns).text
patient_birthdate = patient_data.find('ns0:Patienten_Geburtsdatum', ns).text

# Build the FHIR JSON structure
fhir_json = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": [{
        "resource": {
            "resourceType": "Patient",
            "name": [{
                "family": patient_name,
                "given": [patient_first_name]
            }],
            "gender": "male" if patient_gender == "M" else "female",
            "birthDate": patient_birthdate
        }
    }]
}

# Print the resulting JSON
print(json.dumps(fhir_json, indent=4))
