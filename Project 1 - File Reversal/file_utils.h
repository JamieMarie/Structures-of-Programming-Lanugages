/**
 * This is the interface for the file reversal
 * program. Here, the file and usable functions
 * are defined.
 *
 * @author Jamie Penzien (9/28/17)
**/

#ifndef	__H_FILE_UTILS__
#define __H_FILE_UTILS__

/**
 * This function will take an input of a file-
 * name and a buffer. It will then use those to
 * read the selected file.
 */
int read_file( char* filename, char **buffer );

/**
 * This function will result in an outputted 
 * file with the original file's contents reversed.
 */
int write_file( char* filename, char *buffer, int size );

#endif
