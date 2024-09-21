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
{"resourceType": "Bundle", "type": "transaction", "entry": [{"fullUrl": "Patient/d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937", "resource": {"resourceType": "Patient", "id": "d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937", "meta": {"source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test", "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]}, "identifier": [{"type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "PSEUDED"}, {"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical\u00b7record\u00b7number"}]}, "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id", "value": "1055555888"}], "gender": "male", "birthDate": "1900-07", "address": [{"type": "both", "postalCode": "91000", "country": "DE"}]}, "request": {"method": "PUT", "url": "Patient/d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937"}}]}. The resulting FHIR profile is calles Person. The description of the  FHIR profile is the following: 
<ns0:StructureDefinition xmlns:ns0="http://hl7.org/fhir">
    <ns0:id value="ProfilePatientPatientIn" />
    <ns0:url value="https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/Patient" />
    <ns0:version value="1.0.17" />
    <ns0:name value="ProfilePatientPatientIn" />
    <ns0:title value="Profile - Patient - PatientIn" />
    <ns0:status value="active" />
    <ns0:description value="Dieses Profil beschreibt eine PatientIn in der Medizininformatik-Initiative." />
    <ns0:fhirVersion value="4.0.1" />
    <ns0:kind value="resource" />
    <ns0:abstract value="false" />
    <ns0:type value="Patient" />
    <ns0:baseDefinition value="http://hl7.org/fhir/StructureDefinition/Patient" />
    <ns0:derivation value="constraint" />
    <ns0:differential>
        <ns0:element id="Patient">
            <ns0:path value="Patient" />
            <ns0:constraint>
                <ns0:key value="pat-de-1" />
                <ns0:severity value="error" />
                <ns0:human value="Die amtliche Differenzierung der Geschlechtsangabe 'other' darf nur gefüllt sein, wenn das Geschlecht 'other' angegeben ist" />
                <ns0:expression value="gender='other' or gender.extension('http://fhir.de/StructureDefinition/gender-amtlich-de').empty()" />
                <ns0:source value="https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/Patient" />
            </ns0:constraint>
        </ns0:element>
        <ns0:element id="Patient.id">
            <ns0:path value="Patient.id" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.meta">
            <ns0:path value="Patient.meta" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.meta.source">
            <ns0:path value="Patient.meta.source" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.meta.profile">
            <ns0:path value="Patient.meta.profile" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier">
            <ns0:path value="Patient.identifier" />
            <ns0:slicing>
                <ns0:discriminator>
                    <ns0:type value="pattern" />
                    <ns0:path value="$this" />
                </ns0:discriminator>
                <ns0:rules value="open" />
            </ns0:slicing>
            <ns0:min value="1" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:versichertenId_GKV">
            <ns0:path value="Patient.identifier" />
            <ns0:sliceName value="versichertenId_GKV" />
            <ns0:max value="1" />
            <ns0:type>
                <ns0:code value="Identifier" />
                <ns0:profile value="http://fhir.de/StructureDefinition/identifier-kvid-10" />
            </ns0:type>
            <ns0:patternIdentifier>
                <ns0:type>
                    <ns0:coding>
                        <ns0:system value="http://fhir.de/CodeSystem/identifier-type-de-basis" />
                        <ns0:code value="GKV" />
                    </ns0:coding>
                </ns0:type>
            </ns0:patternIdentifier>
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:versichertenId_GKV.type">
            <ns0:path value="Patient.identifier.type" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:versichertenId_GKV.system">
            <ns0:path value="Patient.identifier.system" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:versichertenId_GKV.value">
            <ns0:path value="Patient.identifier.value" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:versichertenId_GKV.assigner">
            <ns0:path value="Patient.identifier.assigner" />
            <ns0:min value="1" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:versichertenId_GKV.assigner.identifier">
            <ns0:path value="Patient.identifier.assigner.identifier" />
            <ns0:min value="1" />
            <ns0:type>
                <ns0:code value="Identifier" />
                <ns0:profile value="http://fhir.de/StructureDefinition/identifier-iknr" />
            </ns0:type>
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:versichertenId_GKV.assigner.identifier.type">
            <ns0:path value="Patient.identifier.assigner.identifier.type" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:versichertenId_GKV.assigner.identifier.system">
            <ns0:path value="Patient.identifier.assigner.identifier.system" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:versichertenId_GKV.assigner.identifier.value">
            <ns0:path value="Patient.identifier.assigner.identifier.value" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:pid">
            <ns0:path value="Patient.identifier" />
            <ns0:sliceName value="pid" />
            <ns0:type>
                <ns0:code value="Identifier" />
                <ns0:profile value="http://fhir.de/StructureDefinition/identifier-pid" />
            </ns0:type>
            <ns0:patternIdentifier>
                <ns0:type>
                    <ns0:coding>
                        <ns0:system value="http://terminology.hl7.org/CodeSystem/v2-0203" />
                        <ns0:code value="MR" />
                    </ns0:coding>
                </ns0:type>
            </ns0:patternIdentifier>
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:pid.type">
            <ns0:path value="Patient.identifier.type" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:pid.system">
            <ns0:path value="Patient.identifier.system" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:pid.value">
            <ns0:path value="Patient.identifier.value" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:pid.assigner">
            <ns0:path value="Patient.identifier.assigner" />
            <ns0:type>
                <ns0:code value="Reference" />
                <ns0:profile value="https://www.medizininformatik-initiative.de/fhir/core/StructureDefinition/MII-Reference" />
            </ns0:type>
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:pid.assigner.identifier.type">
            <ns0:path value="Patient.identifier.assigner.identifier.type" />
            <ns0:patternCodeableConcept>
                <ns0:coding>
                    <ns0:system value="http://terminology.hl7.org/CodeSystem/v2-0203" />
                    <ns0:code value="XX" />
                </ns0:coding>
            </ns0:patternCodeableConcept>
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:pid.assigner.identifier.system">
            <ns0:path value="Patient.identifier.assigner.identifier.system" />
            <ns0:constraint>
                <ns0:key value="mii-pat-1" />
                <ns0:severity value="error" />
                <ns0:human value="Entweder IKNR oder MII Core Location Identifier soll verwendet werden" />
                <ns0:expression value="$this = 'http://fhir.de/NamingSystem/arge-ik/iknr' or $this = 'https://www.medizininformatik-initiative.de/fhir/core/CodeSystem/core-location-identifier'" />
                <ns0:source value="https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/Patient" />
            </ns0:constraint>
        </ns0:element>
        <ns0:element id="Patient.identifier:versichertennummer_pkv">
            <ns0:path value="Patient.identifier" />
            <ns0:sliceName value="versichertennummer_pkv" />
            <ns0:max value="1" />
            <ns0:type>
                <ns0:code value="Identifier" />
                <ns0:profile value="http://fhir.de/StructureDefinition/identifier-pkv" />
            </ns0:type>
            <ns0:patternIdentifier>
                <ns0:type>
                    <ns0:coding>
                        <ns0:system value="http://fhir.de/CodeSystem/identifier-type-de-basis" />
                        <ns0:code value="PKV" />
                    </ns0:coding>
                </ns0:type>
            </ns0:patternIdentifier>
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:versichertennummer_pkv.use">
            <ns0:path value="Patient.identifier.use" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:versichertennummer_pkv.type">
            <ns0:path value="Patient.identifier.type" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:versichertennummer_pkv.value">
            <ns0:path value="Patient.identifier.value" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:versichertennummer_pkv.assigner">
            <ns0:path value="Patient.identifier.assigner" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:versichertennummer_pkv.assigner.identifier.type">
            <ns0:path value="Patient.identifier.assigner.identifier.type" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:versichertennummer_pkv.assigner.identifier.system">
            <ns0:path value="Patient.identifier.assigner.identifier.system" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:versichertennummer_pkv.assigner.identifier.value">
            <ns0:path value="Patient.identifier.assigner.identifier.value" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.identifier:versichertennummer_pkv.assigner.display">
            <ns0:path value="Patient.identifier.assigner.display" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.name">
            <ns0:path value="Patient.name" />
            <ns0:slicing>
                <ns0:discriminator>
                    <ns0:type value="pattern" />
                    <ns0:path value="$this" />
                </ns0:discriminator>
                <ns0:rules value="open" />
            </ns0:slicing>
            <ns0:min value="1" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.name:name">
            <ns0:path value="Patient.name" />
            <ns0:sliceName value="name" />
            <ns0:min value="1" />
            <ns0:max value="1" />
            <ns0:type>
                <ns0:code value="HumanName" />
                <ns0:profile value="http://fhir.de/StructureDefinition/humanname-de-basis" />
            </ns0:type>
            <ns0:patternHumanName>
                <ns0:use value="official" />
            </ns0:patternHumanName>
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.name:name.use">
            <ns0:path value="Patient.name.use" />
            <ns0:min value="1" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.name:name.family">
            <ns0:path value="Patient.name.family" />
            <ns0:min value="1" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.name:name.family.extension">
            <ns0:path value="Patient.name.family.extension" />
            <ns0:slicing>
                <ns0:discriminator>
                    <ns0:type value="value" />
                    <ns0:path value="url" />
                </ns0:discriminator>
                <ns0:rules value="open" />
            </ns0:slicing>
        </ns0:element>
        <ns0:element id="Patient.name:name.family.extension:namenszusatz">
            <ns0:path value="Patient.name.family.extension" />
            <ns0:sliceName value="namenszusatz" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.name:name.family.extension:nachname">
            <ns0:path value="Patient.name.family.extension" />
            <ns0:sliceName value="nachname" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.name:name.family.extension:vorsatzwort">
            <ns0:path value="Patient.name.family.extension" />
            <ns0:sliceName value="vorsatzwort" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.name:name.given">
            <ns0:path value="Patient.name.given" />
            <ns0:min value="1" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.name:name.prefix">
            <ns0:path value="Patient.name.prefix" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.name:name.prefix.extension">
            <ns0:path value="Patient.name.prefix.extension" />
            <ns0:slicing>
                <ns0:discriminator>
                    <ns0:type value="value" />
                    <ns0:path value="url" />
                </ns0:discriminator>
                <ns0:rules value="open" />
            </ns0:slicing>
        </ns0:element>
        <ns0:element id="Patient.name:name.prefix.extension:prefix-qualifier">
            <ns0:path value="Patient.name.prefix.extension" />
            <ns0:sliceName value="prefix-qualifier" />
            <ns0:max value="1" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.name:geburtsname">
            <ns0:path value="Patient.name" />
            <ns0:sliceName value="geburtsname" />
            <ns0:max value="1" />
            <ns0:type>
                <ns0:code value="HumanName" />
                <ns0:profile value="http://fhir.de/StructureDefinition/humanname-de-basis" />
            </ns0:type>
            <ns0:patternHumanName>
                <ns0:use value="maiden" />
            </ns0:patternHumanName>
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.name:geburtsname.use">
            <ns0:path value="Patient.name.use" />
            <ns0:min value="1" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.name:geburtsname.family">
            <ns0:path value="Patient.name.family" />
            <ns0:min value="1" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.name:geburtsname.family.extension">
            <ns0:path value="Patient.name.family.extension" />
            <ns0:slicing>
                <ns0:discriminator>
                    <ns0:type value="value" />
                    <ns0:path value="url" />
                </ns0:discriminator>
                <ns0:rules value="open" />
            </ns0:slicing>
        </ns0:element>
        <ns0:element id="Patient.name:geburtsname.family.extension:namenszusatz">
            <ns0:path value="Patient.name.family.extension" />
            <ns0:sliceName value="namenszusatz" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.name:geburtsname.family.extension:nachname">
            <ns0:path value="Patient.name.family.extension" />
            <ns0:sliceName value="nachname" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.name:geburtsname.family.extension:vorsatzwort">
            <ns0:path value="Patient.name.family.extension" />
            <ns0:sliceName value="vorsatzwort" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.name:geburtsname.given">
            <ns0:path value="Patient.name.given" />
            <ns0:max value="0" />
        </ns0:element>
        <ns0:element id="Patient.name:geburtsname.prefix">
            <ns0:path value="Patient.name.prefix" />
            <ns0:max value="0" />
        </ns0:element>
        <ns0:element id="Patient.name:geburtsname.prefix.extension">
            <ns0:path value="Patient.name.prefix.extension" />
            <ns0:slicing>
                <ns0:discriminator>
                    <ns0:type value="value" />
                    <ns0:path value="url" />
                </ns0:discriminator>
                <ns0:rules value="open" />
            </ns0:slicing>
        </ns0:element>
        <ns0:element id="Patient.name:geburtsname.prefix.extension:prefix-qualifier">
            <ns0:path value="Patient.name.prefix.extension" />
            <ns0:sliceName value="prefix-qualifier" />
            <ns0:max value="1" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.gender">
            <ns0:path value="Patient.gender" />
            <ns0:min value="1" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.gender.extension">
            <ns0:path value="Patient.gender.extension" />
            <ns0:slicing>
                <ns0:discriminator>
                    <ns0:type value="value" />
                    <ns0:path value="url" />
                </ns0:discriminator>
                <ns0:rules value="open" />
            </ns0:slicing>
        </ns0:element>
        <ns0:element id="Patient.gender.extension:other-amtlich">
            <ns0:path value="Patient.gender.extension" />
            <ns0:sliceName value="other-amtlich" />
            <ns0:max value="1" />
            <ns0:type>
                <ns0:code value="Extension" />
                <ns0:profile value="http://fhir.de/StructureDefinition/gender-amtlich-de" />
            </ns0:type>
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.birthDate">
            <ns0:path value="Patient.birthDate" />
            <ns0:min value="1" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.birthDate.extension">
            <ns0:path value="Patient.birthDate.extension" />
            <ns0:slicing>
                <ns0:discriminator>
                    <ns0:type value="value" />
                    <ns0:path value="url" />
                </ns0:discriminator>
                <ns0:rules value="open" />
            </ns0:slicing>
        </ns0:element>
        <ns0:element id="Patient.birthDate.extension:data-absent-reason">
            <ns0:path value="Patient.birthDate.extension" />
            <ns0:sliceName value="data-absent-reason" />
            <ns0:type>
                <ns0:code value="Extension" />
                <ns0:profile value="http://hl7.org/fhir/StructureDefinition/data-absent-reason" />
            </ns0:type>
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.deceased[x]">
            <ns0:path value="Patient.deceased[x]" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.address">
            <ns0:path value="Patient.address" />
            <ns0:slicing>
                <ns0:discriminator>
                    <ns0:type value="pattern" />
                    <ns0:path value="$this" />
                </ns0:discriminator>
                <ns0:rules value="open" />
            </ns0:slicing>
            <ns0:min value="1" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.address:Strassenanschrift">
            <ns0:path value="Patient.address" />
            <ns0:sliceName value="Strassenanschrift" />
            <ns0:type>
                <ns0:code value="Address" />
                <ns0:profile value="http://fhir.de/StructureDefinition/address-de-basis" />
            </ns0:type>
            <ns0:patternAddress>
                <ns0:type value="both" />
            </ns0:patternAddress>
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.address:Strassenanschrift.extension">
            <ns0:path value="Patient.address.extension" />
            <ns0:slicing>
                <ns0:discriminator>
                    <ns0:type value="value" />
                    <ns0:path value="url" />
                </ns0:discriminator>
                <ns0:rules value="open" />
            </ns0:slicing>
        </ns0:element>
        <ns0:element id="Patient.address:Strassenanschrift.extension:Stadtteil">
            <ns0:path value="Patient.address.extension" />
            <ns0:sliceName value="Stadtteil" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.address:Strassenanschrift.type">
            <ns0:path value="Patient.address.type" />
            <ns0:min value="1" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.address:Strassenanschrift.line">
            <ns0:path value="Patient.address.line" />
            <ns0:min value="1" />
            <ns0:max value="3" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.address:Strassenanschrift.line.extension">
            <ns0:path value="Patient.address.line.extension" />
            <ns0:slicing>
                <ns0:discriminator>
                    <ns0:type value="value" />
                    <ns0:path value="url" />
                </ns0:discriminator>
                <ns0:rules value="open" />
            </ns0:slicing>
        </ns0:element>
        <ns0:element id="Patient.address:Strassenanschrift.line.extension:Strasse">
            <ns0:path value="Patient.address.line.extension" />
            <ns0:sliceName value="Strasse" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.address:Strassenanschrift.line.extension:Hausnummer">
            <ns0:path value="Patient.address.line.extension" />
            <ns0:sliceName value="Hausnummer" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.address:Strassenanschrift.line.extension:Adresszusatz">
            <ns0:path value="Patient.address.line.extension" />
            <ns0:sliceName value="Adresszusatz" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.address:Strassenanschrift.line.extension:Postfach">
            <ns0:path value="Patient.address.line.extension" />
            <ns0:sliceName value="Postfach" />
            <ns0:max value="0" />
        </ns0:element>
        <ns0:element id="Patient.address:Strassenanschrift.city">
            <ns0:path value="Patient.address.city" />
            <ns0:min value="1" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.address:Strassenanschrift.city.extension">
            <ns0:path value="Patient.address.city.extension" />
            <ns0:slicing>
                <ns0:discriminator>
                    <ns0:type value="value" />
                    <ns0:path value="url" />
                </ns0:discriminator>
                <ns0:rules value="open" />
            </ns0:slicing>
        </ns0:element>
        <ns0:element id="Patient.address:Strassenanschrift.city.extension:gemeindeschluessel">
            <ns0:path value="Patient.address.city.extension" />
            <ns0:sliceName value="gemeindeschluessel" />
            <ns0:max value="1" />
            <ns0:type>
                <ns0:code value="Extension" />
                <ns0:profile value="http://fhir.de/StructureDefinition/destatis/ags" />
            </ns0:type>
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.address:Strassenanschrift.postalCode">
            <ns0:path value="Patient.address.postalCode" />
            <ns0:min value="1" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.address:Strassenanschrift.country">
            <ns0:path value="Patient.address.country" />
            <ns0:min value="1" />
            <ns0:constraint>
                <ns0:key value="pat-cnt-2or3-char" />
                <ns0:severity value="warning" />
                <ns0:human value="The content of the country element (if present) SHALL be selected EITHER from ValueSet ISO Country Alpha-2 http://hl7.org/fhir/ValueSet/iso3166-1-2 OR MAY be selected from ISO Country Alpha-3 Value Set http://hl7.org/fhir/ValueSet/iso3166-1-3, IF the country is not specified in value Set ISO Country Alpha-2 http://hl7.org/fhir/ValueSet/iso3166-1-2." />
                <ns0:expression value="country.empty() or (country.memberOf('http://hl7.org/fhir/ValueSet/iso3166-1-2') or country.memberOf('http://hl7.org/fhir/ValueSet/iso3166-1-3'))" />
                <ns0:source value="https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/Patient" />
            </ns0:constraint>
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.address:Postfach">
            <ns0:path value="Patient.address" />
            <ns0:sliceName value="Postfach" />
            <ns0:type>
                <ns0:code value="Address" />
                <ns0:profile value="http://fhir.de/StructureDefinition/address-de-basis" />
            </ns0:type>
            <ns0:patternAddress>
                <ns0:type value="postal" />
            </ns0:patternAddress>
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.address:Postfach.extension">
            <ns0:path value="Patient.address.extension" />
            <ns0:slicing>
                <ns0:discriminator>
                    <ns0:type value="value" />
                    <ns0:path value="url" />
                </ns0:discriminator>
                <ns0:rules value="open" />
            </ns0:slicing>
        </ns0:element>
        <ns0:element id="Patient.address:Postfach.extension:Stadtteil">
            <ns0:path value="Patient.address.extension" />
            <ns0:sliceName value="Stadtteil" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.address:Postfach.type">
            <ns0:path value="Patient.address.type" />
            <ns0:min value="1" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.address:Postfach.line">
            <ns0:path value="Patient.address.line" />
            <ns0:min value="1" />
            <ns0:max value="3" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.address:Postfach.line.extension">
            <ns0:path value="Patient.address.line.extension" />
            <ns0:slicing>
                <ns0:discriminator>
                    <ns0:type value="value" />
                    <ns0:path value="url" />
                </ns0:discriminator>
                <ns0:rules value="open" />
            </ns0:slicing>
        </ns0:element>
        <ns0:element id="Patient.address:Postfach.line.extension:Strasse">
            <ns0:path value="Patient.address.line.extension" />
            <ns0:sliceName value="Strasse" />
            <ns0:max value="0" />
        </ns0:element>
        <ns0:element id="Patient.address:Postfach.line.extension:Hausnummer">
            <ns0:path value="Patient.address.line.extension" />
            <ns0:sliceName value="Hausnummer" />
            <ns0:max value="0" />
        </ns0:element>
        <ns0:element id="Patient.address:Postfach.line.extension:Adresszusatz">
            <ns0:path value="Patient.address.line.extension" />
            <ns0:sliceName value="Adresszusatz" />
            <ns0:max value="0" />
        </ns0:element>
        <ns0:element id="Patient.address:Postfach.line.extension:Postfach">
            <ns0:path value="Patient.address.line.extension" />
            <ns0:sliceName value="Postfach" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.address:Postfach.city">
            <ns0:path value="Patient.address.city" />
            <ns0:min value="1" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.address:Postfach.city.extension">
            <ns0:path value="Patient.address.city.extension" />
            <ns0:slicing>
                <ns0:discriminator>
                    <ns0:type value="value" />
                    <ns0:path value="url" />
                </ns0:discriminator>
                <ns0:rules value="open" />
            </ns0:slicing>
        </ns0:element>
        <ns0:element id="Patient.address:Postfach.city.extension:gemeindeschluessel">
            <ns0:path value="Patient.address.city.extension" />
            <ns0:sliceName value="gemeindeschluessel" />
            <ns0:max value="1" />
            <ns0:type>
                <ns0:code value="Extension" />
                <ns0:profile value="http://fhir.de/StructureDefinition/destatis/ags" />
            </ns0:type>
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.address:Postfach.postalCode">
            <ns0:path value="Patient.address.postalCode" />
            <ns0:min value="1" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.address:Postfach.country">
            <ns0:path value="Patient.address.country" />
            <ns0:min value="1" />
            <ns0:constraint>
                <ns0:key value="pat-cnt-2or3-char" />
                <ns0:severity value="warning" />
                <ns0:human value="The content of the country element (if present) SHALL be selected EITHER from ValueSet ISO Country Alpha-2 http://hl7.org/fhir/ValueSet/iso3166-1-2 OR MAY be selected from ISO Country Alpha-3 Value Set http://hl7.org/fhir/ValueSet/iso3166-1-3, IF the country is not specified in value Set ISO Country Alpha-2 http://hl7.org/fhir/ValueSet/iso3166-1-2." />
                <ns0:expression value="country.empty() or (country.memberOf('http://hl7.org/fhir/ValueSet/iso3166-1-2') or country.memberOf('http://hl7.org/fhir/ValueSet/iso3166-1-3'))" />
                <ns0:source value="https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/Patient" />
            </ns0:constraint>
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.link">
            <ns0:path value="Patient.link" />
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.link.other">
            <ns0:path value="Patient.link.other" />
            <ns0:type>
                <ns0:code value="Reference" />
                <ns0:profile value="https://www.medizininformatik-initiative.de/fhir/core/StructureDefinition/MII-Reference" />
            </ns0:type>
            <ns0:mustSupport value="true" />
        </ns0:element>
        <ns0:element id="Patient.link.type">
            <ns0:path value="Patient.link.type" />
            <ns0:mustSupport value="true" />
        </ns0:element>
    </ns0:differential>
</ns0:StructureDefinition>Create runnable python code for this task that only prints the resulting FHIR json to the console.  Only return the python code! Do not execute it. You can use the xmltodict library to parse the xml file and extract the necessary fields. 

Please note: 
- The resulting FHIR profile is not yet finalized.
- The FHIR profile is currently under development and will change over time. 
- The code you provide must have no dependencies besides Python and xmltodict
- You need to provide an example input XML (as shown in the beginning of the task) and the expected output json (as shown in the beginning of the task) so that we can test your code. 
- You need to use the given FHIR profile to create the resulting FHIR json. 
- You need to handle all possible exceptions that could occur, such as missing fields, invalid input, etc. 
- The code you provide should be self-contained, meaning that it should not rely on external libraries or files. 

Please provide the following information in your submission:
- Python code for converting the given XML to the required FHIR json
- Example input XML and expected output JSON
- FHIR profile used for the conversion
- A brief explanation of how your code works
- Your approach to solving the task

Please note: This task is not related to the MII. Please use the tag "obd-to-fhir" for this task. 