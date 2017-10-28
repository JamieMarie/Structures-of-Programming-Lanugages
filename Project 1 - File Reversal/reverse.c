/**
 * In this main function, the functionalities 
 * of the implemntation file are used to read/
 * write a file reveresed. 
 *
 * @author Jamie Penzien
 */

#include "file_utils.h"
#include <stdio.h>
#include <stdlib.h>

int main( int argc, char** argv ) {

	//Visual display that the program has begun
	printf("================================================================================\n");
	printf("\t\t\tWelcome to the file reversal program.\n");
	printf("================================================================================\n");

	//Creating variables that will be used with the functions
	char *buffer; 
	char *filename1;
	char *filename2;
	int filesize;

	//The readable file will be the first command line argument after calling the program
	filename1 = argv[1];

	//The writable file will be the second command line argument after calling the program
	filename2 = argv[2];

	//The size of the file will be returned from the read_file function
	//The buffer will be loaded with the contents of the first file
	filesize = read_file( filename1, &buffer );

	//Using the contents of the buffer, that info will be written backwards
	//into the second file 
	write_file( filename2, buffer, filesize );

	//notifying the use the program has ended
	printf("\n================================================================================\n");
	printf("\t\t\t\t\tDone\n");

	return 0;

}


