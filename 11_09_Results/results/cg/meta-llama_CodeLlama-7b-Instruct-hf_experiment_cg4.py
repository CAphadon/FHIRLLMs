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
