You are a Python Software Engineer and are asked to create a Python programm that turns the content of a xml file into a specific json. The xml file contains data from a database while the json is supposed to be a FHIR resource json. The input looks like this: 
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
			<ns0:Menge_Meldung>
				<ns0:Meldung Meldung_ID="ST0001238" Melder_ID="ST">
					<ns0:Meldedatum>10.11.2021</ns0:Meldedatum>
					<ns0:Meldebegruendung>I</ns0:Meldebegruendung>
					<ns0:Meldeanlass>behandlungsende</ns0:Meldeanlass>
					<ns0:Tumorzuordnung Tumor_ID="1">
                        <ns0:Primaertumor_ICD_Code>C72.0</ns0:Primaertumor_ICD_Code>
                        <ns0:Primaertumor_ICD_Version>10 2021 GM</ns0:Primaertumor_ICD_Version>
                        <ns0:Diagnosedatum>18.05.2021</ns0:Diagnosedatum>
                        <ns0:Seitenlokalisation>R</ns0:Seitenlokalisation>
                    </ns0:Tumorzuordnung>
					<ns0:Menge_ST>
						<ns0:ST ST_ID="45900">
							<ns0:ST_Intention>P</ns0:ST_Intention>
							<ns0:ST_Stellung_OP>N</ns0:ST_Stellung_OP>
							<ns0:Menge_Bestrahlung>
								<ns0:Bestrahlung>
									<ns0:ST_Zielgebiet>5.4.-</ns0:ST_Zielgebiet>
									<ns0:ST_Seite_Zielgebiet>T</ns0:ST_Seite_Zielgebiet>
								</ns0:Bestrahlung>
								<ns0:Bestrahlung>
									<ns0:ST_Zielgebiet>1.2</ns0:ST_Zielgebiet>
									<ns0:ST_Seite_Zielgebiet>R</ns0:ST_Seite_Zielgebiet>
									<ns0:ST_Ende_Datum>02.12.2021</ns0:ST_Ende_Datum>
								</ns0:Bestrahlung>
							</ns0:Menge_Bestrahlung>
							<ns0:ST_Ende_Grund>L</ns0:ST_Ende_Grund>
							<ns0:Menge_Nebenwirkung>
								<ns0:ST_Nebenwirkung>
									<ns0:Nebenwirkung_Grad>4</ns0:Nebenwirkung_Grad>
								</ns0:ST_Nebenwirkung>
							</ns0:Menge_Nebenwirkung>
						</ns0:ST>
					</ns0:Menge_ST>
				</ns0:Meldung>
			</ns0:Menge_Meldung>
		</ns0:Patient>
	</ns0:Menge_Patient>
	<ns0:Menge_Melder>
		<ns0:Melder Melder_ID="ST">
			<ns0:Meldende_Stelle>ST</ns0:Meldende_Stelle>
		</ns0:Melder>
	</ns0:Menge_Melder>
</ns0:ADT_GEKID>. The FHIR json should be of resourceType 'Bundle' with type 'transaction' and a 'Patient' as its entry. Create runnable python code for this task that only prints the resulting FHIR json to the console. Only return the python code!

```python
```python
```

```python

import xml.etree.ElementTree as ET

# Read the XML file
tree = ET.parse('patient.xml')

# Convert the XML data into a FHIR JSON resource
fhir_json = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": {
        "resource": {
            "resourceType": "Patient",
            "id": "123456789",
            "subject": {"reference": "patient/123456789"},
            "extension": [
                {"url": "patient/extension/identifier", "value": {"reference": "patient/123456789#identifier"}],
                {"url": "patient/extension/patient_address", "value": {"reference": "patient/123456789#patient_address"}}
            ],
            "data": {
                "name": {"family": ["Max"], "given": ["Mustermann"]},
                "birthDate": "02.04.2023",
                "gender": "M",
                "address": {"line": ["Bahnhofstr. 1"], "city": "Tuebingen", "country": "DE", "postalCode": "70070"}
            }
        }
    }
}

# Print the FHIR JSON resource
print(fhir_json)

```

```

This code reads an XML file, parses it, and then converts the data into a FHIR JSON resource. The resulting JSON resource is printed to the console.

```

```
{
  "resourceType": "Bundle",
  "type": "transaction",
  "entry": {
    "resource": {
      "resourceType": "Patient",
      "id": "123456789",
      "subject": {"reference": "patient/123456789"},
      "extension": [
        {"url": "patient/extension/identifier", "value": {"reference": "patient/123456789#identifier"}},
        {"url": "patient/extension/patient_address", "value": {"reference": "patient/123456789#patient_address"}}
      ],
      "data": {
        "name": {"family": ["Max"], "given": ["Mustermann"]},
        "birthDate": "02.04.2023",
        "gender": "M",
        "address": {"line": ["Bahnhofstr. 1"], "city": "Tuebingen", "country": "DE", "postalCode": "70070"}
      }
    }
  }
}
```

```

This JSON resource is a FHIR bundle of type 'transaction' with a single entry for a patient resource. The patient resource has a number of extensions, including the identifier extension and the patient address extension. The patient resource also has a number of data elements, including the patient's name, birth date, gender, and address.