%{
#include<stdio.h>
#incldue "zoomjoystrong.tab.h"
int a = 0;
float b = 0;
float total = 0;
void yyerror(char*);
%}

%option no yywrap

%%
END 			{ return END; }
END_STATEMENT	{ return END_STATEMENT; }
POINT			{ return POINT; }
LINE			{ return LINE; }
CIRCLE			{ return CIRCLE; }
RECTANGLE		{ return RECTANGLE; }
SET_COLOR		{ return SET_COLOR; }
[0-9]+			{ 
					a = yytext[0];
					yylval.ival = atoi(yytext); 
					return INT; 
				}
[0-9]*\.[0-9]+	{ 
					b = yytext[0];
					yyval.fval = atof(yytext); 
					return FLOAT; 
				}
\t | " " | \n	;
,				yyerror("Invalid character.");

%%
int main(int agrc, char** argv){ 
	yylex();
	return 0;
}
