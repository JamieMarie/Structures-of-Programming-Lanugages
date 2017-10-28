%{
	#include <stdio.h>
%}

%option noyywrap

%%

luke|rey|obiwan|revan|yoda		{ return JEDI; }
palptaine|vader|bane|maul|dooku|kylo	{ printf("SITH\N"); }
maz					{ printf("FORCE_SENSITIVE\N"); }
finn					{ printf("UNKNOWN\N"); }
,					{ printf("REDSHIRT\N"); }
\n					;
	
%%
int main(int agrc, char** argv){
	yylex();
	return 0;
}

void println(){
	printf("\n\n");
}
