%{ 
	#include<stdio.h>
	#include<stdlib.h>
	#include "zoomjoystrong.h"
	int yylex();
	int yyerror(char *s);
%}

%start program

%union 
		{ 
			int ival;
			float fval;
		}

%token 	INT
%token	FLOAT
%type<ival> INT
%type<fval> FLOAT
%token 	END		
%token 	END_STATEMENT
%token	POINT
%token	CIRCLE
%token	RECTANGLE
%token	SET_COLOR
%token 	LINE

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

point:	POINT INT INT END_STATEMENT 
	{ point( $2, $3 ); }
	;

line:	LINE INT INT INT INT END_STATEMENT 
	{ line( $2, $3, $4, $5 ); }
	;

circle:	CIRCLE INT INT INT END_STATEMENT 
	{ circle( $2, $3, $4 ); }
	;

setcolor:	SET_COLOR INT INT INT END_STATEMENT 
	{ set_color( $2, $3, $4 ); }
	;

rectangle: RECTANGLE INT INT INT INT END_STATEMENT 
	{ rectangle( $2, $3, $4, $5 ); }
	;

%%
int main()
{
	setup();
	yyparse();
	finish();
	return 0;
}

int yyerror (char *s){
	return fprintf(stderr, "YACC: %s\n", s);
}

int yywrap(){
	return 1;
}
