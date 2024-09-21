import xml.etree.ElementTree as ET
import json
import pprint

tree = ET.fromstring(xml)

def convert(tree):

    def _find(tag, root):
        return root.findall('.//' + tag)

    def _get_text(root):
        return root.text

    def _get_int(root):
        return int(root.text)

    def _get_bool(root):
        return True if root.text == '1' else False

    def _get_float(root):
        return float(root.text)

    def _create_list(root, func):
        lst = []
        if root is not None:
            lst = [func(node) for node in root]
        return lst

    def _create_dict(root, func):
        dct = {}
        if root is not None:
            for node in root:
                key = node.tag.split('}')[-1]
                dct[key] = func(node)
        return dct

    def _create_bundle(root):
        entry_list = _create_list(root.findall('entry'), _create_bundle_entry)
        return {'resourceType': 'Bundle',
                'type': 'transaction',
                'entry': entry_list}

    def _create_bundle_entry(root):
        dct = {}
        dct['fullUrl'] = root.tag.split('}')[-1]
        dct['resource'] = _create_patient(root)
        return dct

    def _create_patient(root):
        dct = _create_dict(root, _create_patient_data)
        return {'resourceType': 'Patient',
                'id': dct['id'],
                'identifier': [
                    {'system': 'http://fhir.de/Namensscheme/FAHND',
                     'value': dct['fahnd']}
                ],
                'name': [
                    {
                        'use': dct['name_use'],
                        'text': dct['name_text'],
                    }
                ],
                'telecom': [
                    {'system': 'phone',
                     'value': dct['phone']},
                ]
                }

    def _create_patient_data(root):
        dct = _create_dict(root, _get_text)
        return {'id': dct['id'],
                'fahnd': dct['fahnd'],
                'name_use': dct['name_use'],
                'name_text': dct['name_text'],
                'phone': dct['phone']}

    # dct = _create_dict(tree, func)
    dct = convert_patient(tree)
    return dct

def convert_patient(tree):
    dct = _create_dict(tree, _get_text)
    return {'resourceType': 'Patient',
            'id': dct['id'],
            'identifier': [
                {'system': 'http://fhir.de/Namensscheme/FAHND',
                 'value': dct['fahnd']}
            ],
            'name': [
                {
                    'use': dct['name_use'],
                    'text': dct['name_text'],
                }
            ],
            'telecom': [
                {'system': 'phone',
                 'value': dct['phone']},
            ]
            }

dct = convert(tree)
print(json.dumps(dct, indent=4))


