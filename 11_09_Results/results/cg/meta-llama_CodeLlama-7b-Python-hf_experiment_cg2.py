import xml.etree.ElementTree as ET
import json

def run(xml_file):
    tree=ET.parse(xml_file)
    root=tree.getroot()
    
    #create bundle
    entry=[]
    #bundle
    b= { "resourceType": "Bundle", "type": "transaction", "entry": entry }
    
    #loop over patients
    for p in root.findall('./ns0:Menge_Patient/ns0:Patient/',{'ns0':'http://www.gekid.de/namespace'}):
        patient_id= p.find('ns0:Patienten_Stammdaten/ns0:Patienten_ID',{'ns0':'http://www.gekid.de/namespace'}).text
        #patient
        patient= { "resourceType": "Patient", "id":patient_id, "meta": { "source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test", "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]}}
        
        #loop over patienten
        for pn in p.findall('ns0:Patienten_Stammdaten/',{'ns0':'http://www.gekid.de/namespace'}):
            #patienten
            if pn.tag=='{http://www.gekid.de/namespace}Patienten_Nachname':
                patient['name']=[{"family":pn.text}]
            elif pn.tag=='{http://www.gekid.de/namespace}Patienten_Vornamen':
                patient['name'][0]['given']=[pn.text]
            elif pn.tag=='{http://www.gekid.de/namespace}Patienten_Geschlecht':
                patient['gender']=pn.text
            elif pn.tag=='{http://www.gekid.de/namespace}Patienten_Geburtsdatum':
                patient['birthDate']=pn.text
        
        #loop over addresses
        for adr in p.findall('ns0:Menge_Adresse/',{'ns0':'http://www.gekid.de/namespace'}):
            #adress
            if 'address' in patient:
                patient['address'].append({"type": "both", "postalCode": adr.find('ns0:Patienten_PLZ',{'ns0':'http://www.gekid.de/namespace'}).text, "country": "DE"})
        
        #loop over melder
        for m in p.findall('ns0:Menge_Melder/',{'ns0':'http://www.gekid.de/namespace'}):
            #melder
            if m.find('ns0:Melder_ID',{'ns0':'http://www.gekid.de/namespace'}).text=='ST':
                #ST
                st={"resourceType": "Organization", "id": "ST", "meta": { "source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test", "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-organization/ActivityDefinition/Organization-Melder"] }, "identifier": [{"type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "ST"}]}, "system": "http://fhir.diz.uk-erlangen.de/identifiers/organization-id", "value": "ST"}]}
                #ST entry
                entry.append({"fullUrl": "Organization/ST", "resource": st})
            
        #loop over meldungen
        for m in p.findall('ns0:Menge_Meldung/',{'ns0':'http://www.gekid.de/namespace'}):
            #meldung
            meldung={"resourceType": "MedicationRequest", "id": m.find('ns0:Meldung_ID',{'ns0':'http://www.gekid.de/namespace'}).text, "meta": { "source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test", "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-medicationrequest/ActivityDefinition/MedicationRequest"] }}
            
            #loop over st
            for st in m.findall('ns0:Menge_ST/',{'ns0':'http://www.gekid.de/namespace'}):
                #st
                st_id= st.find('ns0:ST_ID',{'ns0':'http://www.gekid.de/namespace'}).text
                if st_id not in patient:
                    patient[st_id]={"resourceType": "MedicationRequest", "id": st.find('ns0:ST_ID',{'ns0':'http://www.gekid.de/namespace'}).text, "meta": { "source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test", "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-medicationrequest/ActivityDefinition/MedicationRequest"] }}
                    #append to entry
                    entry.append({"fullUrl": "MedicationRequest/"+st_id, "resource": patient[st_id]})
                
                #medication
                medication={"medicationReference": { "reference": "Medication/"+st_id }}
                
                #st entry
                if 'entry' in patient:
                    patient[st_id]['authoredOn']=m.find('ns0:Meldedatum',{'ns0':'http://www.gekid.de/namespace'}).text
                    patient[st_id]['intent']="authorization"
                    patient[st_id]['status']="on-hold"
                    patient[st_id]['medicationCodeableConcept']={ "text": m.find('ns0:Meldeanlass',{'ns0':'http://www.gekid.de/namespace'}).text }
                    patient[st_id]['subject']={ "reference": "Patient/"+patient_id}
                    patient[st_id]['requester']=[{"reference": "Organization/ST"}]
                    patient[st_id]['contained']=[st]
                    patient[st_id]['authoredOn']=m.find('ns0:Meldedatum',{'ns0':'http://www.gekid.de/namespace'}).text
                    patient[st_id]['intent']="authorization"
                    patient[st_id]['status']="on-hold"
                    patient[st_id]['medicationCodeableConcept']={ "text": m.find('ns0:Meldeanlass',{'ns0':'http://www.gekid.de/namespace'}).text }
                    patient[st_id]['subject']={ "reference": "Patient/"+patient_id}
                    patient[st_id]['requester']=[{"reference": "Organization/ST"}]
                    patient[st_id]['contained']=[st]
                    patient[st_id]['medication']=[medication]
                    patient[st_id]['contained']=[st]
                    #append to entry
                    entry.append({"fullUrl": "MedicationRequest/"+st_id, "resource": patient[st_id]})
        
        #append patient to entry
        entry.append({"fullUrl": "Patient/"+patient_id, "resource": patient})
        
        #print(patient_id)
        #print(json.dumps(patient, indent=4))
        #print(json.dumps(st, indent=4))
        
    
    return json.dumps(b, indent=4)

run('input.xml')
