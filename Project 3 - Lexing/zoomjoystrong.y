%{ 
	#include<stdio.h>
	#include<stdlib.h>
	#undef INT;
	#define INT 258;
	#define FLOAT 259;
	#define END 260;
%}

%start program

%union 
		{ 
			int ival;
			float fval;
		}

%token	<ival> 	INT
%token	<fval>	FLOAT
%token 	END		
%token 	END_STATEMENT
%token	POINT
%token	LINE
%token	CIRCLE
%token	RECTANGLE
%token	SET_COLOR

%%

program:	statement_list END END_STATEMENT
	;

statement_list:		statement
	| statement statement_list
	;

statement:	point
	| line
	| circle
	| setcolor
	| rectangle
	;

point:	POINT 
	INT INT END_STATEMENT
	;

line:	LINE 
	INT INT INT INT END_STATEMENT
	;

circle:	CIRCLE 
	INT INT INT END_STATEMENT
	;

setcolor:	SET_COLOR 
	INT INT INT END_STATEMENT
	/*	if(($2 > 255) || ($3 > 255) || ($4 > 255)) {
       printf("INvalid: Exceeded color limit");
    } */
	;

rectangle: RECTANGLE 
	INT INT INT INT END_STATEMENT
	;




%%
int main()
{
	yyparse();
	return 0;
}

yyerror(s)
char *s;
{
	fprintf(stderr, "%s\n",s);
}

yywrap()
{
	return(1);
}


