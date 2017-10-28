%{ 
	#include <stdio.h>
	#include <stdlib.h>
	float total = 0;
	int iReg = 0;
	float fReg = 0;
%}

%option noyywrap

%%
[0-9]+			{ printf("INT\t%s\n", yytext); iReg = atoi(yytext); } 
[0-9]*\.[0-9]+	{ printf("FLOAT\t%s\n", yytext); fReg = atof(yytext); }
addi			{ total = total + iReg; iReg = 0; printf("Total = %f\n", total); }
addf			{ total = total + fReg; fReg = 0; printf("Total = %f\n", total); }
\*[a-z]			{ printf("Some VAR.\n"); }
.|\n			;

%%

int main(int argc, char** argv){
	yylex();
	return 0;
}
