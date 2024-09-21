from xml.etree import ElementTree
import json

def xml_to_json(file_name):
    tree = ElementTree.parse(file_name)
    root = tree.getroot()
    js = dict()
    js["resourceType"] = "Bundle"
    js["type"] = "transaction"
    js["entry"] = []
    for patient in root.findall("ns0:Menge_Patient", root.nsmap):
        js_pat = dict()
        js_pat["fullUrl"] = "Patient/{0}".format(patient.find("ns0:Patient", root.nsmap).attrib["Patient_ID"])
        js_pat["resource"] = {}
        js_pat["resource"]["resourceType"] = "Patient"
        js_pat["resource"]["id"] = patient.find("ns0:Patient", root.nsmap).attrib["Patient_ID"]
        js_pat["resource"]["meta"] = dict()
        js_pat["resource"]["meta"]["source"] = "{0}.ONKOSTAR:obds-to-fhir:0.0.0-test".format(patient.find("ns0:Absender", root.nsmap).attrib["Absender_ID"])
        js_pat["resource"]["meta"]["profile"] = ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]
        js_pat["resource"]["identifier"] = []
        for identifier in patient.findall("ns0:Patienten_Stammdaten/ns0:Menge_Adresse/ns0:Adresse/ns0:Patienten_Strasse", root.nsmap):
            js_id = dict()
            js_id["type"] = dict()
            js_id["type"]["coding"] = [{"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical\u00b7record\u00b7number"}]
            js_id["system"] = "https://fhir.diz.uk-erlangen.de/identifiers/patient-id"
            js_id["value"] = identifier.text
            js_pat["resource"]["identifier"].append(js_id)
        for identifier in patient.findall("ns0:Patienten_Stammdaten/ns0:KrankenversichertenNr", root.nsmap):
            js_id = dict()
            js_id["type"] = dict()
            js_id["type"]["coding"] = [{"system": "http://fhir.de/CodeSystem/identifier-type-de-basis", "code": "GKV"}]
            js_id["system"] = "http://fhir.de/NamingSystem/arge-ik/iknr"
            js_id["value"] = identifier.text
            js_pat["resource"]["identifier"].append(js_id)
        for identifier in patient.findall("ns0:Patienten_Stammdaten/ns0:KrankenkassenNr", root.nsmap):
            js_id = dict()
            js_id["type"] = dict()
            js_id["type"]["coding"] = [{"system": "http://fhir.de/CodeSystem/identifier-type-de-basis", "code": "PKV"}]
            js_id["system"] = "http://fhir.de/NamingSystem/arge-ik/iknr"
            js_id["value"] = identifier.text
            js_pat["resource"]["identifier"].append(js_id)
        js_pat["resource"]["gender"] = "male" if patient.find("ns0:Patienten_Geschlecht", root.nsmap).text == "M" else "female"
        js_pat["resource"]["birthDate"] = patient.find("ns0:Patienten_Geburtsdatum", root.nsmap).text
        js_pat["resource"]["address"] = []
        for adresse in patient.findall("ns0:Patienten_Stammdaten/ns0:Menge_Adresse/ns0:Adresse/ns0:Patienten_Land", root.nsmap):
            js_adr = dict()
            js_adr["type"] = "both"
            js_adr["postalCode"] = patient.find("ns0:Patienten_Stammdaten/ns0:Menge_Adresse/ns0:Adresse/ns0:Patienten_PLZ", root.nsmap).text
            js_adr["country"] = adresse.text
            js_pat["resource"]["address"].append(js_adr)
        js["entry"].append(js_pat)
    print(json.dumps(js, indent=4, sort_keys=True))

if __name__ == "__main__":
    xml_to_json(input("Please insert input xml file: "))