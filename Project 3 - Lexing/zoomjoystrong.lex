%{
#include<stdio.h>
#include "zoomjoystrong.tab.h"

int ival;
float fval;
void yyerror(char*);
int fileno(FILE *stream);

%}

%option no yywrap

%%
end 			{ return END; }
;				{ return END_STATEMENT; }
point			{ return POINT; }
line			{ return LINE; }
circle			{ return CIRCLE; }
rectangle		{ return RECTANGLE; }
set_color		{ return SET_COLOR; }
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

