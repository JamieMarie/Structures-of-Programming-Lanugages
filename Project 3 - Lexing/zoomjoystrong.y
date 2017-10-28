#include<stdio.h>

%{ 
	/* C code */ 
	#define INT 258
	#define FLOAT 259
%}

%start list

%union 
		{ 
			int a;
			int ival;
			float fval;
		}

%token INT FLOAT

%%

list:		/*empty*/
	 |
	list stat '\n'
	 | 
	list error '\n'
	 {
	   yyerrok;
	 }
	 ;

stat:	expr 		/*expressions*/
	{
	   printf("%d\n",$1);
	}
 	;

expr: 	INT			/*here is options for inputs*/
	 	 |
		FLOAT
		 ;


%%
main()
{
 return(yyparse());
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



