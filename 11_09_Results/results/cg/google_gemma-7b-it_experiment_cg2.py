
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('sample.xml')

# Extract the FHIR JSON from the XML
fhir_json = {"resourceType": "Bundle", "type": "transaction", "entry": [{"fullUrl": "Patient/" + tree.find("ns0:Patienten_Stammdaten").attrib["Patient_ID"], "resource": {"resourceType": "Patient", "id": tree.find("ns0:Patienten_Stammdaten").attrib["Patient_ID"], "meta": {"source": tree.find("ns0:Absender").attrib["Software_ID"] + ":obds-to-fhir:0.0.0-test", "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]}, "identifier": [{"type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "PSEUDED"}, {"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical\u00b7record\u00b7number"}]}, "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id", "value": tree.find("ns0:Patienten_Stammdaten").attrib["Patient_ID"]}], "gender": "male", "birthDate": tree.find("ns0:Patienten_Stammdaten").attrib["Patienten_Geburtsdatum"], "address": [{"type": "both", "postalCode": tree.find("ns0:Adresse").attrib["Patienten_PLZ"], "country": "DE"}]}, "request": {"method": "PUT", "url": "Patient/" + tree.find("ns0:Patienten_Stammdaten").attrib["Patient_ID"]}}]}]}

# Print the FHIR JSON to the console
print(fhir_json)
