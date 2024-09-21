def main():
    # The XML file to be read
    xml_file = 'gekid.xml'
    # The path to the schema file
    schema_path = 'gekid.xsd'

    # Create an XML parser
    parser = etree.XMLParser(schema=schema_path)

    # Parse the XML file
    tree = etree.parse(xml_file, parser)

    # Extract the root node
    root = tree.getroot()

    # Create an empty JSON object
    json = {}

    # Iterate over the child nodes of the root node
    for child in root:
        # Check for the 'Absender' node
        if child.tag == 'Absender':
            # If the 'Absender' node is found, extract the values of its child nodes
            absender_id = child.attrib['Absender_ID']
            software_id = child.attrib['Software_ID']
            installations_id = child.attrib['Installations_ID']
            absender_bezeichnung = child.find('Absender_Bezeichnung').text
            absender_ansprechpartner = child.find('Absender_Ansprechpartner').text
            absender_anschrift = child.find('Absender_Anschrift').text

            # Add the values to the JSON object
            json['resourceType'] = 'Bundle'
            json['type'] = 'transaction'
            json['entry'] = [
                {
                    'fullUrl': 'Patient/123',
                   'resource': {
                       'resourceType': 'Patient',
                        'id': '123',
                       'meta': {
                           'source': '999999.ONKOSTAR:obds-to-fhir:0.0.0-test',
                            'profile': ['https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert']
                        },
                        'identifier': [
                            {
                                'type': {
                                    'coding': [
                                        {
                                           'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationValue',
                                            'code': 'PSEUDED'
                                        },
                                        {
                                           'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                                            'code': 'MR',
                                            'display': 'Medical\u00b7record\u00b7number'
                                        }
                                    ]
                                },
                               'system': 'https://fhir.diz.uk-erlangen.de/identifiers/patient-id',
                                'value': '1055555888'
                            }
                        ],
                        'gender':'male',
                        'birthDate': '1900-07',
                        'address': [
                            {
                                'type': 'both',
                                'postalCode': '91000',
                                'country': 'DE'
                            }
                        ]
                    }
                }
            ]

    # Print the resulting JSON
    print(json)

if __name__ == '__main__':
    main()
