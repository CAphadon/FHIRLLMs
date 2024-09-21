import xml.etree.ElementTree as ET
import json

def xml_to_fhir(xml_string):
    # Parse XML-File
    tree = ET.fromstring(xml_string)
    # Create a new fhir Bundle
    bundle = {}
    bundle['resourceType'] = 'Bundle'
    bundle['type'] = 'transaction'
    # Add patient
    patient = {}
    patient['resourceType'] = 'Patient'
    patient['id'] = tree.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_ID').text
    patient['active'] = True
    patient['name'] = [{
        'family': tree.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_Nachname').text,
        'given': tree.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_Vornamen').text,
        'prefix': tree.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_Titel').text
    }]
    patient['gender'] = tree.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_Geschlecht').text
    patient['birthDate'] = tree.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_Geburtsdatum').text
    bundle['entry'] = [{
       'resource': patient
    }]
    # Add address
    address = {}
    address['resourceType'] = 'Address'
    address['line'] = tree.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_Strasse').text
    address['city'] = tree.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_Ort').text
    address['postalCode'] = tree.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_PLZ').text
    address['country'] = tree.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_Land').text
    patient['address'] = [address]
    # Add identifier
    identifier = {}
    identifier['system'] = 'https://fhir.onki.de/fhir'
    identifier['value'] = tree.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_ID').text
    patient['identifier'] = [identifier]
    # Add telecom
    telecom = {}
    telecom['system'] = 'phone'
    telecom['value'] = tree.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_TelNr').text
    patient['telecom'] = [telecom]
    # Add communication
    communication = {}
    communication['language'] = 'de'
    communication['text'] = tree.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_Sprache').text
    patient['communication'] = [communication]
    # Add extension
    extension = {}
    extension['url'] = 'http://hl7.org/fhir/StructureDefinition/patient-mrn'
    extension['valueIdentifier'] = {}
    extension['valueIdentifier']['system'] = 'https://www.gekid.de/fhir'
    extension['valueIdentifier']['value'] = tree.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}KrankenversichertenNr').text
    patient['extension'] = [extension]
    # Add extension
    extension = {}
    extension['url'] = 'http://hl7.org/fhir/StructureDefinition/patient-mrn'
    extension['valueIdentifier'] = {}
    extension['valueIdentifier']['system'] = 'https://www.gekid.de/fhir'
    extension['valueIdentifier']['value'] = tree.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}KrankenkassenNr').text
    patient['extension'] = [extension]
    # Add extension
    extension = {}
    extension['url'] = 'http://hl7.org/fhir/StructureDefinition/patient-mrn'
    extension['valueIdentifier'] = {}
    extension['valueIdentifier']['system'] = 'https://www.gekid.de/fhir'
    extension['valueIdentifier']['value'] = tree.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Kassenzeichen').text
    patient['extension'] = [extension]
    # Add extension
    extension = {}
    extension['url'] = 'http://hl7.org/fhir/StructureDefinition/patient-mrn'
    extension['valueIdentifier'] = {}
    extension['valueIdentifier']['system'] = 'https://www.gekid.de/fhir'
    extension['valueIdentifier']['value'] = tree.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_ID').text
    patient['extension'] = [extension]
    # Add extension
    extension = {}
    extension['url'] = 'http://hl7.org/fhir/StructureDefinition/patient-mrn'
    extension['valueIdentifier'] = {}
    extension['valueIdentifier']['system'] = 'http://www.gekid.de/fhir'
    extension['valueIdentifier']['value'] = tree.find('{http://www.gekid.de/namespace}Patienten_Stammdaten/{http://www.gekid.de/namespace}Patienten_ID').text
    patient['extension'] = [extension]
    return bundle

# Main
if __name__ == '__main__':
    xml_string = """<ns0:ADT_GEKID xmlns:ns0="http://www.gekid.de/namespace" Schema_Version="2.2.1">
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
</ns0:ADT_GEKID>"""
    print(json.dumps(xml_to_fhir(xml_string), indent=4))
