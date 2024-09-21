from xml.dom.minidom import parseString
import json
with open('test.xml', 'r') as file:
    data = file.read()

dom = parseString(data)

output = ''
output = output + '{\n'
output = output + '"' +'resourceType" : "' + 'Bundle' + '",\n'
output = output + '"' + 'type' + '" : "' + 'transaction' + '",\n'
output = output + '"' + 'entry' + '" : [\n'

for node in dom.getElementsByTagName('ns0:Patienten_Stammdaten'):
    output = output + '{\n'
    output = output + '"' + 'fullUrl' + '" : "' + 'Patient/' + node.getAttribute('Patient_ID') + '",\n'
    output = output + '"' +'resource' + '" : \n'
    output = output + '{\n'
    output = output + '"' +'resourceType' + '" : "' + 'Patient' + '",\n'
    output = output + '"' + 'id' + '" : "' + node.getAttribute('Patient_ID') + '",\n'
    output = output + '"' +'meta' + '" :\n'
    output = output + '{\n'
    output = output + '"' +'source' + '" : "' + node.parentNode.parentNode.getAttribute('Absender_ID') + '.ONKOSTAR:obds-to-fhir:0.0.0-test",\n'
    output = output + '"' + 'profile' + '" : [ "https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert" ]\n'
    output = output + '},\n'
    output = output + '"' + 'identifier' + '" : [\n'
    output = output + '{\n'
    output = output + '"' + 'type' + '" :\n'
    output = output + '{\n'
    output = output + '"' + 'coding' + '" : [\n'
    output = output + '{\n'
    output = output + '"' +'system' + '" : "http://terminology.hl7.org/CodeSystem/v3-ObservationValue",\n'
    output = output + '"' + 'code' + '" : "PSEUDED",\n'
    output = output + '"' + 'display' + '" : "Patient\u00b7record\u00b7number"\n'
    output = output + '}\n'
    output = output + '],\n'
    output = output + '"' +'system' + '" : "https://fhir.diz.uk-erlangen.de/identifiers/patient-id",\n'
    output = output + '"' + 'value' + '" : "' + node.getAttribute('KrankenversichertenNr') + '"\n'
    output = output + '}\n'
    output = output + '],\n'
    output = output + '"' + 'gender' + '" : "' + node.getAttribute('Patienten_Geschlecht') + '",\n'
    output = output + '"' + 'birthDate' + '" : "' + node.getAttribute('Patienten_Geburtsdatum') + '",\n'
    output = output + '"' + 'address' + '" : [\n'
    output = output + '{\n'
    output = output + '"' + 'type' + '" : "both",\n'
    output = output + '"' + 'postalCode' + '" : "' + node.getElementsByTagName('ns0:Patienten_PLZ')[0].childNodes[0].data + '",\n'
    output = output + '"' + 'country' + '" : "' + node.getElementsByTagName('ns0:Patienten_Land')[0].childNodes[0].data + '"\n'
    output = output + '}\n'
    output = output + ']\n'
    output = output + '}\n'

output = output + ']\n'
output = output + '}\n'

output = output + ']\n'
output = output + '}\n'

print(output)



