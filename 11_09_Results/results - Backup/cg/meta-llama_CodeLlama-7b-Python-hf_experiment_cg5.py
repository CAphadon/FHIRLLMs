You are a Python Software Engineer and are asked to create a Python programm that turns the content of a xml file into a FHIR json. The input looks like this: 
<ns0:ADT_GEKID xmlns:ns0="http://www.gekid.de/namespace" Schema_Version="2.2.1">
	<ns0:Absender Absender_ID="22222244" Software_ID="ONKOSTAR" Installations_ID="2.9.8">
		<ns0:Absender_Bezeichnung>UKER</ns0:Absender_Bezeichnung>
		<ns0:Absender_Ansprechpartner />
		<ns0:Absender_Anschrift>Maximiliansplatz 2, 91054 Erlangen</ns0:Absender_Anschrift>
	</ns0:Absender>
	<ns0:Menge_Patient>
		<ns0:Patient>
            <ns0:Patienten_Stammdaten Patient_ID="123456789">
                <ns0:KrankenversichertenNr>Q123456</ns0:KrankenversichertenNr>
                <ns0:KrankenkassenNr>555555</ns0:KrankenkassenNr>
                <ns0:Patienten_Nachname>Max</ns0:Patienten_Nachname>
                <ns0:Patienten_Vornamen>Mustermann</ns0:Patienten_Vornamen>
                <ns0:Patienten_Geschlecht>M</ns0:Patienten_Geschlecht>
                <ns0:Patienten_Geburtsdatum>02.04.2023</ns0:Patienten_Geburtsdatum>
                <ns0:Menge_Adresse>
                    <ns0:Adresse>
                        <ns0:Patienten_Strasse>Bahnhofstr. 1</ns0:Patienten_Strasse>
                        <ns0:Patienten_Land>DE</ns0:Patienten_Land>
                        <ns0:Patienten_PLZ>70070</ns0:Patienten_PLZ>
                        <ns0:Patienten_Ort>Tuebingen</ns0:Patienten_Ort>
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
</ns0:ADT_GEKID>. The FHIR json should be of resourceType 'Bundle' with type 'transaction' and a 'Patient' as its entry. The runnable python code for this task that only prints the resulting FHIR json to the console looks like this: 

<pre><code class="language-python">from xml.dom import minidom 
import xml.dom.minidom 
from xml.dom import minidom 
import xml.dom.minidom 
import json 
import xmltodict 
import urllib.request 
import urllib.parse 
import urllib.error 
import xmltodict 
import json 
import xml.etree.ElementTree as ET 
import xml.dom.minidom as DOM 
import urllib.request 
import urllib.parse 
import urllib.error 
import json 
from xml.dom import minidom 
from xml.dom import minidom 
import xml.dom.minidom 
import xml.dom.minidom 
from xml.dom import minidom 
from xml.dom import minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom 
import xml.dom.minidom


doc = minidom.parse('data.xml')
root = doc.documentElement
print(root.tagName)


root.tagName


root.firstChild.tagName


root.firstChild.firstChild.tagName


root.firstChild.firstChild.firstChild.tagName


root.firstChild.firstChild.firstChild.firstChild.tagName


root.firstChild.firstChild.firstChild.firstChild.firstChild.tagName


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.tagName


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.tagName


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.getAttribute('Schema_Version')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.getAttribute('Absender_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.getAttribute('Installations_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[1].firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[3].firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[4].firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[5].firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[7].firstChild.firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[7].firstChild.childNodes[1].firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[7].firstChild.childNodes[1].firstChild.getAttribute('Absender_Bezeichnung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[7].firstChild.childNodes[1].firstChild.getAttribute('Absender_Ansprechpartner')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[7].firstChild.childNodes[1].firstChild.getAttribute('Absender_Anschrift')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[9].firstChild.firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[9].firstChild.childNodes[1].firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[9].firstChild.childNodes[1].firstChild.getAttribute('Patienten_Stammdaten')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[9].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('Patient_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[9].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('KrankenversichertenNr')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[9].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('KrankenkassenNr')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[9].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('Patienten_Nachname')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[9].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('Patienten_Vornamen')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[9].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('Patienten_Geschlecht')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[9].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('Patienten_Geburtsdatum')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[9].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('Menge_Adresse')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[9].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('Patienten_Strasse')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[9].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('Patienten_Land')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[9].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('Patienten_PLZ')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[9].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('Patienten_Ort')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.getAttribute('Meldung_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.getAttribute('Melder_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.getAttribute('Meldedatum')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.getAttribute('Meldebegruendung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.getAttribute('Meldeanlass')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.getAttribute('ST_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.getAttribute('ST_Intention')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.getAttribute('ST_Stellung_OP')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('Bestrahlung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('ST_Zielgebiet')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('ST_Seite_Zielgebiet')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('ST_Ende_Datum')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('Nebenwirkung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('Nebenwirkung_Grad')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.firstChild.getAttribute('Absender_Bezeichnung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.firstChild.getAttribute('Absender_Ansprechpartner')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.firstChild.getAttribute('Absender_Anschrift')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.firstChild.getAttribute('Menge_Bestrahlung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('Bestrahlung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.firstChild.getAttribute('ST_Zielgebiet')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.firstChild.getAttribute('ST_Seite_Zielgebiet')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.firstChild.getAttribute('ST_Ende_Datum')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.firstChild.getAttribute('Nebenwirkung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[11].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.firstChild.getAttribute('Nebenwirkung_Grad')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[13].firstChild.firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[13].firstChild.childNodes[1].firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[13].firstChild.childNodes[1].firstChild.getAttribute('Meldung_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[13].firstChild.childNodes[1].firstChild.getAttribute('Melder_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[13].firstChild.childNodes[1].firstChild.getAttribute('Meldedatum')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[13].firstChild.childNodes[1].firstChild.getAttribute('Meldebegruendung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[13].firstChild.childNodes[1].firstChild.getAttribute('Meldeanlass')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[13].firstChild.childNodes[1].firstChild.getAttribute('ST_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[13].firstChild.childNodes[1].firstChild.getAttribute('ST_Intention')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[13].firstChild.childNodes[1].firstChild.getAttribute('ST_Stellung_OP')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[13].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('Bestrahlung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[13].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('ST_Zielgebiet')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[13].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('ST_Seite_Zielgebiet')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[13].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('ST_Ende_Datum')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[13].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('Nebenwirkung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[13].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.childNodes[1].firstChild.getAttribute('Nebenwirkung_Grad')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[15].firstChild.firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[15].firstChild.childNodes[1].firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[15].firstChild.childNodes[1].firstChild.getAttribute('Menge_Melder')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[17].firstChild.firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[17].firstChild.childNodes[1].firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[17].firstChild.childNodes[1].firstChild.getAttribute('Meldung_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[17].firstChild.childNodes[1].firstChild.getAttribute('Melder_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[17].firstChild.childNodes[1].firstChild.getAttribute('Meldedatum')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[17].firstChild.childNodes[1].firstChild.getAttribute('Meldebegruendung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[17].firstChild.childNodes[1].firstChild.getAttribute('Meldeanlass')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[17].firstChild.childNodes[1].firstChild.getAttribute('ST_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[17].firstChild.childNodes[1].firstChild.getAttribute('ST_Intention')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[17].firstChild.childNodes[1].firstChild.getAttribute('ST_Stellung_OP')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[17].firstChild.childNodes[1].firstChild.getAttribute('Nebenwirkung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[17].firstChild.childNodes[1].firstChild.getAttribute('Nebenwirkung_Grad')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[19].firstChild.firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[19].firstChild.childNodes[1].firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[19].firstChild.childNodes[1].firstChild.getAttribute('Meldung_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[19].firstChild.childNodes[1].firstChild.getAttribute('Melder_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[19].firstChild.childNodes[1].firstChild.getAttribute('Meldedatum')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[19].firstChild.childNodes[1].firstChild.getAttribute('Meldebegruendung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[19].firstChild.childNodes[1].firstChild.getAttribute('Meldeanlass')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[19].firstChild.childNodes[1].firstChild.getAttribute('ST_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[19].firstChild.childNodes[1].firstChild.getAttribute('ST_Intention')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[19].firstChild.childNodes[1].firstChild.getAttribute('ST_Stellung_OP')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[19].firstChild.childNodes[1].firstChild.getAttribute('Nebenwirkung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[19].firstChild.childNodes[1].firstChild.getAttribute('Nebenwirkung_Grad')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[21].firstChild.firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[21].firstChild.childNodes[1].firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[21].firstChild.childNodes[1].firstChild.getAttribute('Meldung_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[21].firstChild.childNodes[1].firstChild.getAttribute('Melder_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[21].firstChild.childNodes[1].firstChild.getAttribute('Meldedatum')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[21].firstChild.childNodes[1].firstChild.getAttribute('Meldebegruendung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[21].firstChild.childNodes[1].firstChild.getAttribute('Meldeanlass')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[21].firstChild.childNodes[1].firstChild.getAttribute('ST_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[21].firstChild.childNodes[1].firstChild.getAttribute('ST_Intention')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[21].firstChild.childNodes[1].firstChild.getAttribute('ST_Stellung_OP')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[21].firstChild.childNodes[1].firstChild.getAttribute('Nebenwirkung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[21].firstChild.childNodes[1].firstChild.getAttribute('Nebenwirkung_Grad')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[23].firstChild.firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[23].firstChild.childNodes[1].firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[23].firstChild.childNodes[1].firstChild.getAttribute('Meldung_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[23].firstChild.childNodes[1].firstChild.getAttribute('Melder_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[23].firstChild.childNodes[1].firstChild.getAttribute('Meldedatum')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[23].firstChild.childNodes[1].firstChild.getAttribute('Meldebegruendung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[23].firstChild.childNodes[1].firstChild.getAttribute('Meldeanlass')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[23].firstChild.childNodes[1].firstChild.getAttribute('ST_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[23].firstChild.childNodes[1].firstChild.getAttribute('ST_Intention')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[23].firstChild.childNodes[1].firstChild.getAttribute('ST_Stellung_OP')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[23].firstChild.childNodes[1].firstChild.getAttribute('Nebenwirkung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[23].firstChild.childNodes[1].firstChild.getAttribute('Nebenwirkung_Grad')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[25].firstChild.firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[25].firstChild.childNodes[1].firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[25].firstChild.childNodes[1].firstChild.getAttribute('Meldung_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[25].firstChild.childNodes[1].firstChild.getAttribute('Melder_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[25].firstChild.childNodes[1].firstChild.getAttribute('Meldedatum')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[25].firstChild.childNodes[1].firstChild.getAttribute('Meldebegruendung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[25].firstChild.childNodes[1].firstChild.getAttribute('Meldeanlass')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[25].firstChild.childNodes[1].firstChild.getAttribute('ST_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[25].firstChild.childNodes[1].firstChild.getAttribute('ST_Intention')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[25].firstChild.childNodes[1].firstChild.getAttribute('ST_Stellung_OP')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[25].firstChild.childNodes[1].firstChild.getAttribute('Nebenwirkung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[25].firstChild.childNodes[1].firstChild.getAttribute('Nebenwirkung_Grad')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[27].firstChild.firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[27].firstChild.childNodes[1].firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[27].firstChild.childNodes[1].firstChild.getAttribute('Meldung_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[27].firstChild.childNodes[1].firstChild.getAttribute('Melder_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[27].firstChild.childNodes[1].firstChild.getAttribute('Meldedatum')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[27].firstChild.childNodes[1].firstChild.getAttribute('Meldebegruendung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[27].firstChild.childNodes[1].firstChild.getAttribute('Meldeanlass')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[27].firstChild.childNodes[1].firstChild.getAttribute('ST_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[27].firstChild.childNodes[1].firstChild.getAttribute('ST_Intention')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[27].firstChild.childNodes[1].firstChild.getAttribute('ST_Stellung_OP')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[27].firstChild.childNodes[1].firstChild.getAttribute('Nebenwirkung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[27].firstChild.childNodes[1].firstChild.getAttribute('Nebenwirkung_Grad')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[29].firstChild.firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[29].firstChild.childNodes[1].firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[29].firstChild.childNodes[1].firstChild.getAttribute('Meldung_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[29].firstChild.childNodes[1].firstChild.getAttribute('Melder_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[29].firstChild.childNodes[1].firstChild.getAttribute('Meldedatum')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[29].firstChild.childNodes[1].firstChild.getAttribute('Meldebegruendung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[29].firstChild.childNodes[1].firstChild.getAttribute('Meldeanlass')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[29].firstChild.childNodes[1].firstChild.getAttribute('ST_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[29].firstChild.childNodes[1].firstChild.getAttribute('ST_Intention')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[29].firstChild.childNodes[1].firstChild.getAttribute('ST_Stellung_OP')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[29].firstChild.childNodes[1].firstChild.getAttribute('Nebenwirkung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[29].firstChild.childNodes[1].firstChild.getAttribute('Nebenwirkung_Grad')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[31].firstChild.firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[31].firstChild.childNodes[1].firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[31].firstChild.childNodes[1].firstChild.getAttribute('Meldung_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[31].firstChild.childNodes[1].firstChild.getAttribute('Melder_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[31].firstChild.childNodes[1].firstChild.getAttribute('Meldedatum')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[31].firstChild.childNodes[1].firstChild.getAttribute('Meldebegruendung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[31].firstChild.childNodes[1].firstChild.getAttribute('Meldeanlass')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[31].firstChild.childNodes[1].firstChild.getAttribute('ST_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[31].firstChild.childNodes[1].firstChild.getAttribute('ST_Intention')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[31].firstChild.childNodes[1].firstChild.getAttribute('ST_Stellung_OP')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[31].firstChild.childNodes[1].firstChild.getAttribute('Nebenwirkung')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[31].firstChild.childNodes[1].firstChild.getAttribute('Nebenwirkung_Grad')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[33].firstChild.firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[33].firstChild.childNodes[1].firstChild.nodeValue


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[33].firstChild.childNodes[1].firstChild.getAttribute('Meldung_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[33].firstChild.childNodes[1].firstChild.getAttribute('Melder_ID')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[33].firstChild.childNodes[1].firstChild.getAttribute('Meldedatum')


root.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.childNodes[33].firstChild.child