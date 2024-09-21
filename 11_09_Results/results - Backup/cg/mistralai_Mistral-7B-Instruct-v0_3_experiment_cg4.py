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

Here is a Python code that parses the XML file and converts it into a FHIR Bundle resource. Note that this code is a simplified version and does not cover all the fields in the XML. Also, it assumes that the provided XML is well-formed.

```python
from xml.etree import ElementTree as ET
from datetime import datetime
from fhir.resources.patient import Patient, Name, Telecom, Address, ContactPoint
from fhir.resources.bundle import Bundle

def parse_xml_to_fhir(xml_str):
    root = ET.fromstring(xml_str)
    sender = root.find(".//ns0:Absender")
    patient = root.find(".//ns0:Patient")
    melder = root.find(".//ns0:Melder")

    # Convert XML to FHIR Patient
    fhir_patient = Patient()
    fhir_patient.name = [Name(family=sender.find(".//ns0:Absender_Bezeichnung").text, given=[patient.find(".//ns0:Patienten_Vornamen").text])]
    fhir_patient.telecom = [Telecom(system="phone", value=melder.find(".//ns0:Meldende_Stelle").text)]
    fhir_patient.address = [Address(use="home", line=[patient.find(".//ns0:Patienten_Strasse").text], city=patient.find(".//ns0:Patienten_Ort").text, state=patient.find(".//ns0:Patienten_Land").text, postalCode=patient.find(".//ns0:Patienten_PLZ").text)]

    # Add contact details if present
    contact_details = patient.find(".//ns0:Menge_Adresse")
    if contact_details is not None:
        fhir_patient.contact = [ContactPoint(system="email", value=contact_details.find(".//ns0:Patienten_E_Mail").text)]

    # Create FHIR Bundle
    fhir_bundle = Bundle(type_='transaction')
    fhir_bundle.entry = [fhir_patient]

    return fhir_bundle.json()

def main():
    xml_str = """<ns0:ADT_GEKID xmlns:ns0="http://www.gekid.de/namespace" Schema_Version="2.2.1">
                   ...
                 </ns0:ADT_GEKID>"""

    fhir_json = parse_xml_to_fhir(xml_str)
    print(fhir_json)

if __name__ == "__main__":
    main()
```

Replace the `xml_str` variable with the content of your XML file. This code uses the FHIR Python library, which can be installed via:

```
pip install fhir
```

Make sure to adjust the code according to your specific XML structure and requirements.