	#include <stdio.h>
	#include "y.tab.h"
	void foo(){
		printf("Trabalho 2 - Yacc:\n");
	}
%}

%%
[0-9]+                 return DIGITO;
[a-z]              return LETRA_MINUSCULA;
[A-Z]              return LETRA_MAISCULA;
[ \t\n]+              /*ignora espaço em branco*/;
[+, -]                      return SINAL; 

[{digit}+"."{digit}]+   return NUMERO_REAL;
[a-zA-Z]*            return PALAVRA;
[a-zA-Z0-9_]*       return PALAVRA;
[("program")|("var")|("if")|("else")|("then")|("while")|("do")|("for")|("begin")|("end")|("integer")|("real")|("read")|("write")|("ident")|("repeat")|("writeln")|("nomep")|("readln")|("until")] return PALAVRA-RESERVADA;
 [(":")|("=")|(";")|(",")|("(")|(")")|(">")|(">=")|("<")|("<=")|("+")|("-")|("/")|("*")|("{")|("}")|("!")|("%")] return SIMBOLO;
[("@")|("#")|("$")|("&")]                  return SIMBOLO_INVALIDO;
%%
