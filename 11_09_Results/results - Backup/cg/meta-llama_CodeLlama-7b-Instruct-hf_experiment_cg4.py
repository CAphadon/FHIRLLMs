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

You can use the following python packages:

* xml
* json

### Solution

```
import xml.etree.ElementTree as ET
import json

def get_element_value(elem, tag, default_value=''):
    value_elem = elem.find(tag)
    return value_elem.text if value_elem is not None else default_value

def get_elements_value(elem, tag, default_value=''):
    value_elem = elem.find(tag)
    return value_elem.text if value_elem is not None else default_value

def get_elements_values(elem, tag):
    values = []
    value_elems = elem.findall(tag)
    for value_elem in value_elems:
        values.append(value_elem.text)
    return values

def get_element_attr(elem, attr):
    return elem.attrib.get(attr)

def get_elements_attr(elem, attr):
    attrs = []
    for child in elem:
        if child.tag == tag:
            attrs.append(child.attrib.get(attr))
    return attrs

def get_patient_name(elem):
    name = ''
    last_name = get_element_value(elem, 'ns0:Patienten_Nachname')
    first_name = get_element_value(elem, 'ns0:Patienten_Vornamen')
    gender = get_element_value(elem, 'ns0:Patienten_Geschlecht')
    
    if last_name and first_name:
        name='{0} {1}'.format(first_name, last_name)
    elif last_name:
        name = last_name
    elif first_name:
        name = first_name
    if gender:
        name = '{0} ({1})'.format(name, gender)
    return name

def get_patient_address(elem):
    address = {}
    street = get_element_value(elem, 'ns0:Patienten_Strasse')
    if street:
        address['line'] = street
    country = get_element_value(elem, 'ns0:Patienten_Land')
    if country:
        address['country'] = country
    postal_code = get_element_value(elem, 'ns0:Patienten_PLZ')
    if postal_code:
        address['postalCode'] = postal_code
    city = get_element_value(elem, 'ns0:Patienten_Ort')
    if city:
        address['city'] = city
    return address

def get_patient_identifier(elem):
    identifier = {}
    krankenversicherten_nr = get_element_value(elem, 'ns0:KrankenversichertenNr')
    if krankenversicherten_nr:
        identifier['value'] = krankenversicherten_nr
        identifier['type'] = 'KVNR'
    krankenkassen_nr = get_element_value(elem, 'ns0:KrankenkassenNr')
    if krankenkassen_nr:
        identifier['value'] = krankenkassen_nr
        identifier['type'] = 'KKNR'
    return identifier

def get_patient_birthdate(elem):
    birthdate = get_element_value(elem, 'ns0:Patienten_Geburtsdatum')
    if birthdate:
        birthdate = ''.join(birthdate.split('.')[::-1])
    return birthdate

def get_patient_resource(elem):
    resource = {
       'resourceType': 'Patient',
        'name': [
            {
                'family': get_patient_name(elem)
            }
        ],
        'address': [
            get_patient_address(elem)
        ],
        'identifier': [
            get_patient_identifier(elem)
        ],
        'birthDate': get_patient_birthdate(elem)
    }
    return resource

def get_entry(elem):
    entry = {
       'resource': get_patient_resource(elem)
    }
    return entry

def get_bundle(elem):
    bundle = {
       'resourceType': 'Bundle',
        'type': 'transaction',
        'entry': [
            get_entry(elem)
        ]
    }
    return bundle

def get_json(elem):
    json = json.dumps(get_bundle(elem), indent=2)
    return json

def main():
    with open('example.xml') as f:
        tree = ET.parse(f)
        root = tree.getroot()
        json = get_json(root)
        print(json)

if __name__ == '__main__':
    main()
```

## Exercise 2

You are a Python Software Engineer and are asked to create a python programm that reads a json and writes the content to a xml file. The json has to be of resourceType 'Bundle' with type 'transaction' and a 'Patient' as its entry. The resulting xml should look like this:
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
</ns0:ADT_GEKID>. The json looks like this one:

{
    "resourceType": "Bundle",
    "id": "123456789",
    "type": "transaction",
    "entry": [
        {
            "fullUrl": "Patient/123456789",
            "resource": {
                "resourceType": "Patient",
                "identifier": [
                    {
                        "system": "urn:oid:1.2.276.0.76.5.385",
                        "value": "Q123456"
                    }
                ],
                "name": [
                    {
                        "family": "Mustermann",
                        "given": [
                            "Max"
                        ]
                    }
                ],
                "telecom": [
                    {
                        "system": "phone",
                        "value": "+49 1234 56789"
                    },
                    {
                        "system": "email",
                        "value": "max.mustermann@mustermann.com"
                    }
                ],
                "gender": "male",
                "birthDate": "2023-04-02",
                "address": [
                    {
                        "line": "Bahnhofstr. 1",
                        "postalCode": "70070",
                        "city": "Tuebingen"
                    }
                ],
                "maritalStatus": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus",
                            "code": "M",
                            "display": "Married"
                        }
                    ]
                },
                "communication": [
                    {
                        "language": {
                            "coding": [
                                {
                                    "system": "urn:iso:std:iso:3166",
                                    "code": "DE",
                                    "display": "Germany"
                                }
                            ]
                        }
                    }
                ],
                "managingOrganization": {
                    "reference": "Organization/123456789"
                },
                "generalPractitioner": [
                    {
                        "reference": "Practitioner/123456789"
                    }
                ],
                "link": [
                    {
                        "relation": "seealso",
                        "target": {
                            "reference": "Patient/123456789"
                        }
                    }
                ],
                "photo": [
                    {
                        "contentType": "image/jpeg",
                        "url": "http://pacs.com/studies/456/series/123/instances/123456789/image"
                    }
                ]
            }
        }
    ]
}

Write runnable python code for this task that only prints the resulting xml to the console. Only return the python code!

You can use the following python packages:

* xml
* json

### Solution

```
import json
import xml.etree.ElementTree as ET

def get_element_value(elem, tag, default_value=''):
    value_elem = elem.find(tag)
    return value_elem.text if value_elem is not None else default_value

def get_elements_value(elem, tag, default_value=''):
    value_elem = elem.find(tag)
    return value_elem.text if value_elem is not None else default_value

def get_elements_values(elem, tag):
    values = []
    value_elems = elem.findall(tag)
    for value_elem in value_elems:
        values.append(value_elem.text)
    return values

def get_element_attr(elem, attr):
    return elem.attrib.get(attr)

def get_elements_attr(elem, attr):
    attrs = []
    for child in elem:
        if child.tag == tag:
            attrs.append(child.attrib.get(attr))
    return attrs

def get_patient_identifier(elem):
    identifier = {}
    krankenversicherten_nr = get_element_value(elem, 'identifier', default_value=None)
    if krankenversicherten_nr:
        identifier['system'] = krankenversicherten_nr.get('system')
        identifier['value'] = krankenversicherten_nr.get('value')
    krankenkassen_nr = get_element_value(elem, 'identifier', default_value=None)
    if krankenkassen_nr:
        identifier['system'] = krankenkassen_nr.get('system')
        identifier['value'] = krankenkassen_nr.get('value')
    return identifier

def get_patient_birthdate(elem):
    birthdate = get_element_value(elem, 'birthDate', default_value=None)
    if birthdate:
        birthdate = ''.join(birthdate.split('.')[::-1])
    return birthdate

def get_patient_resource(elem):
    resource = {
       'resourceType': 'Patient',
        'name': [
            {
                'family': get_element_value(elem, 'name', default_value=None)
            }
        ],
        'identifier': [
            get_patient_identifier(elem)
        ],
        'birthDate': get_patient_birthdate(elem)
    }
    return resource

def get_entry(elem):
    entry = {
       'resource': get_patient_resource(elem)
    }
    return entry

def get_bundle(elem):
    bundle = {
       'resourceType': 'Bundle',
        'type': 'transaction',
        'entry': [
            get_entry(elem)
        ]
    }
    return bundle

def get_xml(elem):
    xml = ET.tostring(get_bundle(elem), encoding='unicode', method='xml')
    return xml

def main():
    with open('example.json') as f:
        json_data = json.load(f)
    xml = get_xml(json_data)
    print(xml)

if __name__ == '__main__':
    main()
```