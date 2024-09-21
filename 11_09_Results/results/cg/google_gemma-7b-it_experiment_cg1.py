import xml.etree.ElementTree as ET

# Read the XML file
tree = ET.parse("patient.xml")

# Convert the XML to a dictionary
json_data = ET.todict(tree)

# Print the JSON data to the console
print(json_data)
