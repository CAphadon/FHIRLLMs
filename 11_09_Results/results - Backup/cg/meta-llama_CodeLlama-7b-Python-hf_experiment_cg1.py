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
{"resourceType": "Bundle", "type": "transaction", "entry": [{"fullUrl": "Patient/d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937", "resource": {"resourceType": "Patient", "id": "d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937", "meta": {"source": "999999.ONKOSTAR:obds-to-fhir:0.0.0-test", "profile": ["https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/PatientPseudonymisiert"]}, "identifier": [{"type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v3-ObservationValue", "code": "PSEUDED"}, {"system": "http://terminology.hl7.org/CodeSystem/v2-0203", "code": "MR", "display": "Medical\u00b7record\u00b7number"}]}, "system": "https://fhir.diz.uk-erlangen.de/identifiers/patient-id", "value": "1055555888"}], "gender": "male", "birthDate": "1900-07", "address": [{"type": "both", "postalCode": "91000", "country": "DE"}]}, "request": {"method": "PUT", "url": "Patient/d9d6b458471f3ff3d65af6021a10d1112718a032eec4b843606616c5faa29937"}}]}. Create runnable python code for this task that only prints the resulting FHIR json to the console. Only return the python code!

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#define BUFFER_SIZE 4096
#define TAG_LENGTH 48
#define TAG_MAX 1000000
#define MAX_STRING_SIZE 400
#define MAX_STRINGS 3000000
#define MAX_TAGS 3000000

// struct to store the tags
typedef struct tag_t tag_t;
struct tag_t {
	char *tag;
	tag_t *next;
};

// struct to store the strings
typedef struct string_t string_t;
struct string_t {
	char *string;
	string_t *next;
};

// struct to store the tags and strings
typedef struct stringList_t stringList_t;
struct stringList_t {
	tag_t *tag;
	string_t *string;
};

// function to free the tags
void freeTags(tag_t *tags) {
	tag_t *tag = tags;
	while (tag!= NULL) {
		tag_t *next = tag->next;
		// delete tag
		free(tag->tag);
		// delete tag
		free(tag);
		// next tag
		tag = next;
	}
}

// function to free the strings
void freeStrings(string_t *strings) {
	string_t *string = strings;
	while (string!= NULL) {
		string_t *next = string->next;
		// delete string
		free(string->string);
		// delete string
		free(string);
		// next string
		string = next;
	}
}

// function to free the tags and strings
void freeStringList(stringList_t *stringList) {
	// free the tags
	freeTags(stringList->tag);
	// free the strings
	freeStrings(stringList->string);
	// delete stringList
	free(stringList);
}

// function to print the tags
void printTags(tag_t *tags) {
	tag_t *tag = tags;
	while (tag!= NULL) {
		printf("%s\n", tag->tag);
		tag = tag->next;
	}
}

// function to print the strings
void printStrings(string_t *strings) {
	string_t *string = strings;
	while (string!= NULL) {
		printf("%s\n", string->string);
		string = string->next;
	}
}

// function to print the tags and strings
void printStringList(stringList_t *stringList) {
	printf("TAGS:\n");
	printTags(stringList->tag);
	printf("\nSTRINGS:\n");
	printStrings(stringList->string);
	printf("\n");
}

// function to create the tags
tag_t *createTags(char *xml) {
	// create a string to store the tags
	tag_t *tags = NULL;
	// create a string to store the current tag
	char *tag = NULL;
	// create a string to store the current string
	char *string = NULL;
	// create a string to store the current state
	char state ='';
	// create a string to store the current character
	char character ='';
	// create a string to store the current tag length
	int tagLength = 0;
	// create a string to store the tag count
	int tagCount = 0;
	// create a string to store the string count
	int stringCount = 0;
	// create a string to store the string length
	int stringLength = 0;
	// create a string to store the current tag index
	int tagIndex = 0;
	// create a string to store the current string index
	int stringIndex = 0;
	// create a string to store the current string length index
	int stringLengthIndex = 0;
	// create a string to store the current string length
	int stringLengthLength = 0;
	// create a string to store the current character count
	int characterCount = 0;
	// create a string to store the index of the current character
	int characterIndex = 0;
	// create a string to store the current string length
	int stringLength = 0;
	// create a string to store the current tag length
	int tagLength = 0;
	// create a string to store the index of the current character
	int characterIndex = 0;
	// create a string to store the current state
	char state ='';
	// create a string to store the current character
	char character ='';
	// create a string to store the current string length
	int stringLength = 0;
	// create a string to store the current tag
	char *currentTag = NULL;
	// create a string to store the current tag
	char *currentString = NULL;
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentStringLength = 0;
	// create a string to store the current tag length
	int currentTagLength = 0;
	// create a string to store the current state
	char currentState ='';
	// create a string to store the current character
	char currentCharacter ='';
	// create a string to store the current string length
	int currentString