import xml.etree.ElementTree as ET

# Read the XML file
tree = ET.parse("patient.xml")

# Convert the XML tree into a JSON dictionary
json_data = json.dumps(dict(tree.attrib) | dict(tree.findall(".//text") | map(lambda node: {"fullUrl": node.attrib["fullUrl"], "resource": dict(node.attrib) & dict(node.findall(".//text") | map(lambda n: {"type": {"coding": [{"system": n.attrib["system"], "code": n.attrib["code"]}], "value": n.text}))})))

# Print the JSON data to the console
print(json_data)