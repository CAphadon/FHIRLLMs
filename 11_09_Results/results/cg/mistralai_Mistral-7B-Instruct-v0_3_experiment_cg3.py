import xml.etree.ElementTree as ET
import json
from fhir.resources.patient import Patient
from fhir.models.r4.backboneelement import BackboneElement
from fhir.models.r4.codeableconcept import CodeableConcept
from fhir.models.r4.reference import Reference
from fhir.models.r4.identifier import Identifier
from fhir.models.r4.humanname import HumanName
from fhir.models.r4.address import Address
from fhir.models.r4.codetype import CodeType
from fhir.models.r4.extension import Extension
from fhir.models.r4.structuredefinition import StructureDefinition
from lxml import etree

def convert_xml_to_fhir(xml_data):
    xml_root = ET.fromstring(xml_data)
    patient = Patient()
    patient.id = xml_root.attrib.get("PatientID")

    absender = BackboneElement()
    absender.codeable_concept = CodeableConcept(text=xml_root.find(".//{http://www.gekid.de/namespace}Absender_Bezeichnung").text)
    absender_element = xml_root.find(".//{http://www.gekid.de/namespace}Absender")
    if absender_element.find(".//{http://www.gekid.de/namespace}Absender_Ansprechpartner"):
        absender.extension.append(Extension(url="https://fhir.de/StructureDefinition/absender-ansprechpartner", valueCodeableConcept=CodeableConcept(text=absender_element.find(".//{http://www.gekid.de/namespace}Absender_Ansprechpartner").text)))
    absender.address = Address()
    absender_address_element = absender_element.find(".//{http://www.gekid.de/namespace}Absender_Anschrift")
    absender.address.line = [absender_address_element.find(".//{http://www.gekid.de/namespace}Absender_Strasse").text]
    absender.address.city = absender_address_element.find(".//{http://www.gekid.de/namespace}Absender_Ort").text
    absender.address.country = "DE"

    patient.meta.profile = ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]
    patient.identifier = []
    patient_identifier = Identifier()
    patient_identifier.system = "https://fhir.diz.uk-erlangen.de/identifiers/patient-id"
    patient_identifier.value = xml_root.attrib.get("PatientID")
    patient.identifier.append(patient_identifier)
    patient_identifier_versichertennummer_GKV = Identifier()
    patient_identifier_versichertennummer_GKV.system = "https://fhir.de/NamingSystem/arge-ik/iknr"
    patient_identifier_versichertennummer_GKV.use = "official"
    patient_identifier_versichertennummer_GKV.value = xml_root.attrib.get("PatientID")
    patient.identifier.append(patient_identifier_versichertennummer_GKV)

    # Add Patient Name
    name = HumanName()
    name.family = [xml_root.find(".//{http://www.gekid.de/namespace}Absender_Bezeichnung").text]
    patient.name = [name]

    # Add Patient Gender
    gender = patient.gender
    gender.coding = [CodeType(system="http://terminology.hl7.org/CodeSystem/gender", code="male")]
    gender.extension.append(Extension(url="https://fhir.de/StructureDefinition/gender-amtlich-de", valueCodeableConcept=CodeableConcept(text="M")))

    # Add Patient BirthDate
    birthdate = patient.birthDate
    birthdate.value = xml_root.attrib.get("Patient_Geburtsdatum")

    # Add Patient Address
    #... (Assuming the address is already in the format of the FHIR Address resource)

    return json.dumps(patient.primitive_data(), indent=2)

def main():
    xml_data = """<ns0:ADT_GEKID xmlns:ns0="http://www.gekid.de/namespace" Schema_Version="2.2.1">
        <ns0:Absender Absender_ID="999999" Software_ID="ONKOSTAR" Installations_ID="2.9.8">
            <ns0:Absender_Bezeichnung>UKER</ns0:Absender_Bezeichnung>
            <ns0:Absender_Ansprechpartner />
            <ns0:Absender_Anschrift>Maximiliansplatz 2, 91054 Erlangen</ns0:Absender_Anschrift>
        </ns0:Absender>
        <ns0:Menge_Patient>
            <ns0:Patient>
                <ns0:Patienten_Stammdaten Patient_ID="1055555888">
                    <ns0:KrankenversichertenNr>Q00000000</ns0:KrankenversichertenNr>
                    <ns0:KrankenkassenNr>10000000</ns0:KrankenkassenNr>
                    <ns0:Patienten_Nachname>Doe</ns0:Patienten_Nachname>
                    <ns0:Patienten_Vornamen>John</ns0:Patienten_Vornamen>
                    <ns0:Patienten_Geschlecht>M</ns0:Patienten_Geschlecht>
                    <ns0:Patienten_Geburtsdatum>11.09.1900</ns0:Patienten_Geburtsdatum>
                    <ns0:Menge_Adresse>
                        <ns0:Adresse>
                            <ns0:Patienten_Strasse>Johnstr. 7</ns0:Patienten_Strasse>
                            <ns0:Patienten_Land>DE</ns0:Patienten_Land>
                            <ns0:Patienten_PLZ>91000</ns0:Patienten_PLZ>
                            <ns0:Patienten_Ort>Johncity</ns0:Patienten_Ort>
                        </ns0:Adresse>
                    </ns0:Menge_Adresse>
                </ns0:Patienten_Stammdaten>
            </ns0:Patient>
        </ns0:Menge_Patient>
    </ns0:ADT_GEKID>"""
    fhir_json = convert_xml_to_fhir(xml_data)
    print(fhir_json)

if __name__ == "__main__":
    main()
