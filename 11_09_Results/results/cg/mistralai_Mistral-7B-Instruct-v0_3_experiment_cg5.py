import xml.etree.ElementTree as ET
import json
from datetime import datetime
from fhir.resources.patient import Patient
from fhir.resources.bundle import Bundle
from fhir.resources.medicationrequest import MedicationRequest
from fhir.resources.medicationstatement import MedicationStatement
from fhir.resources.procedure import Procedure

def xml_to_dict(xml_str):
    root = ET.fromstring(xml_str)
    result = {}
    for elem in root.iter():
        key = elem.tag.split('}')[-1]
        value = ET.tostring(elem, encoding='utf-8', method='elements').decode('utf-8')
        result[key] = value
    return result

def dict_to_fhir_patient(input_dict):
    patient = Patient()
    patient.name = [
        {
            'family': input_dict['ns0:Patienten_Nachname'],
            'given': [input_dict['ns0:Patienten_Vornamen']]
        }
    ]
    patient.birthDate = input_dict['ns0:Patienten_Geburtsdatum']
    patient.gender = 'M' if input_dict['ns0:Patienten_Geschlecht'] == 'M' else 'F'
    address = {
        'use': 'home',
        'text': input_dict['ns0:Menge_Adresse'],
        'line': [
            input_dict['ns0:Patienten_Strasse'].split(',')[0]
        ],
        'city': input_dict['ns0:Patienten_Ort'],
       'state': input_dict['ns0:Patienten_Land'],
        'postalCode': input_dict['ns0:Patienten_PLZ']
    }
    patient.address = [address]
    patient.telecom = [{
       'system': 'phone',
        'value': '0123456789'
    }]
    if 'ns0:KrankenversichertenNr' in input_dict:
        patient.identifier = [{
           'system': 'https://www.example.com/identifiers',
            'value': input_dict['ns0:KrankenversichertenNr']
        }]
    if 'ns0:KrankenkassenNr' in input_dict:
        patient.identifier = patient.identifier + [{
           'system': 'https://www.example.com/identifiers',
            'value': input_dict['ns0:KrankenkassenNr']
        }]
    return patient

def fhir_patient_to_json(fhir_patient):
    return json.dumps(fhir_patient.to_dict(), indent=4, default=lambda x: str(x))

def xml_to_fhir_json(xml_str: str):
    input_dict = xml_to_dict(xml_str)
    patient = dict_to_fhir_patient(input_dict)
    bundle = Bundle(
        type='transaction'
    )
    bundle.entry.append(patient)
    return json.dumps(bundle.to_dict(), indent=4)

if __name__ == '__main__':
    xml_str = '<ns0:ADT_GEKID xmlns:ns0="http://www.gekid.de/namespace" Schema_Version="2.2.1">\
        <ns0:Absender Absender_ID="22222244" Software_ID="ONKOSTAR" Installations_ID="2.9.8">\
            <ns0:Absender_Bezeichnung>UKER</ns0:Absender_Bezeichnung>\
            <ns0:Absender_Ansprechpartner />\
            <ns0:Absender_Anschrift>Maximiliansplatz 2, 91054 Erlangen</ns0:Absender_Anschrift>\
        </ns0:Absender>\
        <ns0:Menge_Patient>\
            <ns0:Patient>\
                <ns0:Patienten_Stammdaten Patient_ID="123456789">\
                    <ns0:KrankenversichertenNr>Q123456</ns0:KrankenversichertenNr>\
                    <ns0:KrankenkassenNr>555555</ns0:KrankenkassenNr>\
                    <ns0:Patienten_Nachname>Max</ns0:Patienten_Nachname>\
                    <ns0:Patienten_Vornamen>Mustermann</ns0:Patienten_Vornamen>\
                    <ns0:Patienten_Geschlecht>M</ns0:Patienten_Geschlecht>\
                    <ns0:Patienten_Geburtsdatum>02.04.2023</ns0:Patienten_Geburtsdatum>\
                    <ns0:Menge_Adresse>\
                        <ns0:Adresse>\
                            <ns0:Patienten_Strasse>Bahnhofstr. 1</ns0:Patienten_Strasse>\
                            <ns0:Patienten_Land>DE</ns0:Patienten_Land>\
                            <ns0:Patienten_PLZ>70070</ns0:Patienten_PLZ>\
                            <ns0:Patienten_Ort>Tuebingen</ns0:Patienten_Ort>\
                        </ns0:Adresse>\
                    </ns0:Menge_Adresse>\
                </ns0:Patienten_Stammdaten>\
                <ns0:Menge_Meldung>\
                    <ns0:Meldung Meldung_ID="ST0001238" Melder_ID="ST">\
                        <ns0:Meldedatum>10.11.2021</ns0:Meldedatum>\
                        <ns0:Meldebegruendung>I</ns0:Meldebegruendung>\
                        <ns0:Meldeanlass>behandlungsende</ns0:Meldeanlass>\
                        <ns0:Tumorzuordnung Tumor_ID="1">\
                            <ns0:Primaertumor_ICD_Code>C72.0</ns0:Primaertumor_ICD_Code>\
                            <ns0:Primaertumor_ICD_Version>10 2021 GM</ns0:Primaertumor_ICD_Version>\
                            <ns0:Diagnosedatum>18.05.2021</ns0:Diagnosedatum>\
                            <ns0:Seitenlokalisation>R</ns0:Seitenlokalisation>\
                        </ns0:Tumorzuordnung>\
                        <ns0:Menge_ST>\
                            <ns0:ST ST_ID="45900">\
                                <ns0:ST_Intention>P</ns0:ST_Intention>\
                                <ns0:ST_Stellung_OP>N</ns0:ST_Stellung_OP>\
                                <ns0:Menge_Bestrahlung>\
                                    <ns0:Bestrahlung>\
                                        <ns0:ST_Zielgebiet>5.4.-</ns0:ST_Zielgebiet>\
                                        <ns0:ST_Seite_Zielgebiet>T</ns0:ST_Seite_Zielgebiet>\
                                    </ns0:Bestrahlung>\
                                    <ns0:Bestrahlung>\
                                        <ns0:ST_Zielgebiet>1.2</ns0:ST_Zielgebiet>\
                                        <ns0:ST_Seite_Zielgebiet>R</ns0:ST_Seite_Zielgebiet>\
                                        <ns0:ST_Ende_Datum>02.12.2021</ns0:ST_Ende_Datum>\
                                    </ns0:Bestrahlung>\
                                </ns0:Menge_Bestrahlung>\
                                <ns0:ST_Ende_Grund>L</ns0:ST_Ende_Grund>\
                                <ns0:Menge_Nebenwirkung>\
                                    <ns0:ST_Nebenwirkung>\
                                        <ns0:Nebenwirkung_Grad>4</ns0:Nebenwirkung_Grad>\
                                    </ns0:ST_Nebenwirkung>\
                                </ns0:Menge_Nebenwirkung>\
                            </ns0:ST>\
                        </ns0:Menge_ST>\
                    </ns0:Meldung>\
                </ns0:Menge_Meldung>\
            </ns0:Patient>\
        </ns0:Menge_Patient>\
        <ns0:Menge_Melder>\
            <ns0:Melder Melder_ID="ST">\
                <ns0:Meldende_Stelle>ST</ns0:Meldende_Stelle>\
            </ns0:Melder>\
        </ns0:Menge_Melder>\
    </ns0:ADT_GEKID>'
    print(xml_to_fhir_json(xml_str))
