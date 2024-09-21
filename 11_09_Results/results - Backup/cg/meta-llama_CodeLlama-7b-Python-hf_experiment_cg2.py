You are a Python Software Engineer and are asked to create a Python programm that turns the content of a xml file into a specific json. The xml file contains data from a database while the json is supposed to be a FHIR resource json. The input looks like this: 
<ns0:ADT_GEKID xmlns:ns0="http://www.gekid.de/namespace" Schema_Version="2.2.1">
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
			<ns0:Menge_Meldung>
				<ns0:Meldung Meldung_ID="ST0001238" Melder_ID="ST">
					<ns0:Meldedatum>10.11.2021</ns0:Meldedatum>
					<ns0:Meldebegruendung>I</ns0:Meldebegruendung>
					<ns0:Meldeanlass>behandlungsende</ns0:Meldeanlass>
					<ns0:Tumorzuordnung Tumor_ID="1">
                        <ns0:Primaertumor_ICD_Code>C72.0</ns0:Primaertumor_ICD_Code>
                        <ns0:Primaertumor_ICD_Version>10 2021 GM</ns0:Primaertumor_ICD_Version>
                        <ns0:Diagnosedatum>18.05.2021</ns0:Diagnosedatum>
                        <ns0:Seitenlokalisation>R</ns0:Seitenlokalisation>
                    </ns0:Tumorzuordnung>
					<ns0:Menge_ST>
						<ns0:ST ST_ID="45900">
							<ns0:ST_Intention>P</ns0:ST_Intention>
							<ns0:ST_Stellung_OP>N</ns0:ST_Stellung_OP>
							<ns0:Menge_Bestrahlung>
								<ns0:Bestrahlung>
									<ns0:ST_Zielgebiet>5.4.-</ns0:ST_Zielgebiet>
									<ns0:ST_Seite_Zielgebiet>T</ns0:ST_Seite_Zielgebiet>
								</ns0:Bestrahlung>
								<ns0:Bestrahlung>
									<ns0:ST_Zielgebiet>1.2</ns0:ST_Zielgebiet>
									<ns0:ST_Seite_Zielgebiet>R</ns0:ST_Seite_Zielgebiet>
									<ns0:ST_Ende_Datum>02.12.2021</ns0:ST_Ende_Datum>
								</ns0:Bestrahlung>
							</ns0:Menge_Bestrahlung>
							<ns0:ST_Ende_Grund>L</ns0:ST_Ende_Grund>
							<ns0:Menge_Nebenwirkung>
								<ns0:ST_Nebenwirkung>
									<ns0:Nebenwirkung_Grad>4</ns0:Nebenwirkung_Grad>
								</ns0:ST_Nebenwirkung>
							</ns0:Menge_Nebenwirkung>
						</ns0:ST>
					</ns0:Menge_ST>
				</ns0:Meldung>
			</ns0:Menge_Meldung>
		</ns0:Patient>
	</ns0:Menge_Patient>
	<ns0:Menge_Melder>
		<ns0:Melder Melder_ID="ST">
			<ns0:Meldende_Stelle>ST</ns0:Meldende_Stelle>
		</ns0:Melder>
	</ns0:Menge_Melder>
</ns0:ADT_GEKID> while the output should look like this: 
{"resourceType": "Bundle", "type": "transaction", "entry": [{"fullUrl": "Patient/d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937", "resource": {"resourceType": "Patient", "id": "d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937", "meta": {"source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test", "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]}, "identifier": [{"type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "PSEUDED"}, {"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical\u00b7record\u00b7number"}]}, "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id", "value": "1055555888"}], "gender": "male", "birthDate": "1900-07", "address": [{"type": "both", "postalCode": "91000", "country": "DE"}]}, "request": {"method": "PUT", "url": "Patient/d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937"}}]}. The resulting FHIR profile is called Person. Create runnable python code for this task that only prints the resulting FHIR json to the console.  Only return the python code!

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
