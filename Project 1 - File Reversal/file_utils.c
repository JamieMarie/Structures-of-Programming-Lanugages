/**
 * This file will provide executable actions
 * for the functions that were created in the
 * header file. 
 * 
 * @author Jamie Penzien (10/2/17)
 */

#include "file_utils.h"
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h> 

/**
 * This function will read the information within
 * the file provided via the parameters. It will 
 * insert that information into the buffer so 
 * that it can read it later and write it to a 
 * file. 
 */
int read_file( char* filename, char **buffer ){

	//Notifying the user the process has begun
	printf( "\t\t\t You have begun to read the file.\n" );

	//A variable representing the size of the file
	int size = 0;

	//Creating a file using the filename provided in param
	FILE *file1;

	//Telling the system we will be reading what's within the file
	file1 = fopen(filename, "r");

	//Checking whether the file exists or not 
	if( file1 == NULL ) {

		printf("================================================================================\n");
		fprintf( stderr, "\t\t\t   ERROR: File does not exist.\n" );
		printf("================================================================================\n");
	
	} else {

		//Code provided by Prof. Woodring to read size of file.
		struct stat st;
		stat( filename, &st );
		size = st.st_size;
		
		//Allocating space within the buffer the size of the file provided
		*buffer = ( char* )malloc( size );
		
		//Check whether or not the buffer was successfully created
		if( buffer == NULL ) {

			printf("================================================================================\n");
			fprintf( stderr, "\t\t\t   ERROR: Problem allocating memory.\n" );
			printf("================================================================================\n");
		
		} else {	
			//Read the information within file1 and put it into the buffer 
			fread( *buffer, 1, size, file1 );
	
			//Notifying the user that the reading has finished
			printf( "\t\t\t  You successfully read the file.\n" );
		}
	}

	//Returning the size of the file
	return size; 
}


/**
 * This function will open the file provided. It will 
 * then go through the file in reverse order, printing as 
 * it does so. The function returns one after the reversal
 * of a file.  
 */
int write_file( char* filename, char *buffer, int size ){
	
	//Notifying the user the process has started
	printf("\t\t\tYou have begun to write to the file.\n");

	//Creating a FILE using the filename provided within param
	FILE* file2; 

	//Notifying the System we will be writing to this file 
	//IF IT EXISTS - it will empty and then write to that file 
	//IF IT DOES NOT EXIST - it will create the file 
	file2 = fopen( filename, "w");

	//Checking to make sure the buffer has the file information in it
	//AKA that the read file function has been called on it
	if( buffer == NULL ) {

		printf("================================================================================\n");
		fprintf( stderr, "\t\t\t   ERROR: Problem allocating memory.\n" ); 
		printf("================================================================================\n");
	
	} else {

		//Looping through the buffer (file contents) BACKWARDS
		for( int i = size - 1; i >= 0; i--) {

			//Pointer to current data within the buffer 			
			char* j = buffer + i;

			//Printing the current pointing spot of the file contents to 
			//the new file: file2
			fprintf( file2, "%c", *j );
		}
		
		//Notifying the user the program has finished writing
		printf( "\t\t\tYou successfully wrote to the file.\n" );
	}
	
	//Returning a 1 
	return 1; 
}

