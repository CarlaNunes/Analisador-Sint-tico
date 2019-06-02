%{
	#include <stdio.h>
	#include "y.tab.h"
	void foo(){
		printf("Trabalho 2 - Yacc:\n");
	}
%}

%%
digit [0-9]+                 return DIGITO;
letter [a-zA-Z]              return LETRA;
space [ \t\n]+              /*ignora espaço em branco*/;
sign [+, -]                      return SINAL; 
num_int -?{digit}({digit})*      return NUMERO_INTEIRO;
num_real -?{digit}+"."{digit}+   return NUMERO_REAL;
word [a-zA-Z][a-zA-Z0-9_]*       return PALAVRA;
palavra_reservada ("program")|("var")|("if")|("else")|("then")|("while")|("do")|("for")|("begin")|("end")|("integer")|("real")|("read")|("write")|("ident")|("repeat")|("writeln")|("nomep")|("readln")|("until") return PALAVRA-RESERVADA;
simb (":")|("=")|(";")|(",")|("(")|(")")|(">")|(">=")|("<")|("<=")|("+")|("-")|("/")|("*")|("{")|("}")|("!")|("%") return SIMBOLO;
invalid_simb ("@")|("#")|("$")|("&")                  return SIMBOLO_INVALIDO;
%%
