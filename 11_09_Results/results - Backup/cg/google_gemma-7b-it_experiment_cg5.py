You are a Python Software Engineer and are asked to create a Python programm that turns the content of a xml file into a FHIR json. The input looks like this: 
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
</ns0:ADT_GEKID>. The FHIR json should be of resourceType 'Bundle' with type 'transaction' and a 'Patient' as its entry. The runnable python code for this task that only prints the resulting FHIR json to the console looks like this:

```python
import xml.etree.ElementTree as ET

# Read the XML file
tree = ET.parse("patient.xml")

# Convert the XML data into a FHIR JSON
fhir_json = convert_xml_to_fhir_json(tree)

# Print the FHIR JSON
print(fhir_json)
```

**Please provide me with the complete code that turns the XML file content into a FHIR json.**

```python
import xml.etree.ElementTree as ET

# Read the XML file
tree = ET.parse("patient.xml")

# Convert the XML data into a FHIR JSON
fhir_json = convert_xml_to_fhir_json(tree)

# Print the FHIR JSON
print(fhir_json)
```

**Additional notes:**

* The code should use the `convert_xml_to_fhir_json()` function to convert the XML data into a FHIR JSON.
* The FHIR JSON should be of resourceType 'Bundle' with type 'transaction' and a 'Patient' as its entry.
* The FHIR JSON should include all of the data from the XML file.

**Example:**

**XML file:**

```xml
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
</ns0:ADT_GEKID>
```

**Output:**

```
{
  "resourceType": "Bundle",
  "type": "transaction",
  "entry": [
    {
      "resource": {
        "resourceType": "Patient",
        "id": "123456789",
        "patient": {
          "patientIdentifier": [{
            "system": "Q123456",
            "value": "555555"
          }],
          "name": {"family": "Mustermann", "given": ["Max"]},
          "birthDate": "02.04.2023",
          "address": {
            "addressLine": ["Bahnhofstr. 1"],
            "city": "Tuebingen",
            "country": "DE",
            "postalCode": "70070"
          }
        },
        "encounter": [{
          "id": "ST0001238",
          "type": "inpatient",
          "subject": {"reference": "Patient/123456789"},
          "encounterDatetime": "10.11.2021",
          "reason": "behandlungsende",
          "diagnosis": [{
            "code": "C72.0",
            "version": "10 2021 GM",
            "date": "18.05.2021",
            "laterality": "R"
          }],
          "treatment": [{
            "intent": "P",
            "procedure": [{
              "code": "ST",
              "laterality": "N"
            }],
            "radiation": [{
              "targetSite": "5.4.-"
            }],
            "pharmaceuticals": [{
              "drug": "ST",
              "dose": "4"
            }]
          }],
          "notes": ["L"]
        }]
      }
    }
  ]
}
```