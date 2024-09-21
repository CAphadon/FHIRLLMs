from xml.etree import ElementTree as ET
from datetime import datetime
from fhir.resources.patient import Patient, Name, Telecom, Address, ContactPoint
from fhir.resources.bundle import Bundle

def parse_xml_to_fhir(xml_str):
    root = ET.fromstring(xml_str)
    sender = root.find(".//ns0:Absender")
    patient = root.find(".//ns0:Patient")
    melder = root.find(".//ns0:Melder")

    # Convert XML to FHIR Patient
    fhir_patient = Patient()
    fhir_patient.name = [Name(family=sender.find(".//ns0:Absender_Bezeichnung").text, given=[patient.find(".//ns0:Patienten_Vornamen").text])]
    fhir_patient.telecom = [Telecom(system="phone", value=melder.find(".//ns0:Meldende_Stelle").text)]
    fhir_patient.address = [Address(use="home", line=[patient.find(".//ns0:Patienten_Strasse").text], city=patient.find(".//ns0:Patienten_Ort").text, state=patient.find(".//ns0:Patienten_Land").text, postalCode=patient.find(".//ns0:Patienten_PLZ").text)]

    # Add contact details if present
    contact_details = patient.find(".//ns0:Menge_Adresse")
    if contact_details is not None:
        fhir_patient.contact = [ContactPoint(system="email", value=contact_details.find(".//ns0:Patienten_E_Mail").text)]

    # Create FHIR Bundle
    fhir_bundle = Bundle(type_='transaction')
    fhir_bundle.entry = [fhir_patient]

    return fhir_bundle.json()

def main():
    xml_str = """<ns0:ADT_GEKID xmlns:ns0="http://www.gekid.de/namespace" Schema_Version="2.2.1">
                   ...
                 </ns0:ADT_GEKID>"""

    fhir_json = parse_xml_to_fhir(xml_str)
    print(fhir_json)

if __name__ == "__main__":
    main()
