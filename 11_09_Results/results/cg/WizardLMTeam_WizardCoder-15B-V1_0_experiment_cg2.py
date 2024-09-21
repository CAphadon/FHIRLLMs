import xml.etree.ElementTree as ET
import json

# create xml element tree object
tree = ET.parse('input.xml')

# create root element
root = tree.getroot()

# initialize empty list for resources
resources = []

# iterate over all elements in the xml tree
for elem in root.iter():
    # check if element is a resource
    if elem.tag.startswith('{http://www.gekid.de/namespace}'):
        # create empty dictionary for resource
        resource = {}
        # iterate over all attributes of the current element
        for attr in elem.attrib:
            # add attribute to resource dictionary with key attribute_name and value attribute_value
            resource[attr.split('}')[1]] = elem.attrib[attr]
        # add resource to the list of resources
        resources.append(resource)

# print the resulting list of resources as json
print(json.dumps(resources, indent=4))

