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