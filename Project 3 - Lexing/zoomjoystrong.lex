%{
#include<stdio.h>
#include "zoomjoystrong.tab.h"

int ival;
float fval;
void yyerror(char*);

%}

%option no yywrap

%%
END 			{ return END; }
;				{ return END_STATEMENT; }
POINT			{ return POINT; }
LINE			{ return LINE; }
CIRCLE			{ return CIRCLE; }
RECTANGLE		{ return RECTANGLE; }
SET_COLOR		{ return SET_COLOR; }
[0-9]+			{ 
					yylval.ival = atoi(yytext); 
					return INT; 
				}
[0-9]*\.[0-9]+	{ 
					yylval.fval = atof(yytext); 
					return FLOAT; 
				}
[\t]|" "|[\n]	;
,				yyerror("Invalid character.");

%%

