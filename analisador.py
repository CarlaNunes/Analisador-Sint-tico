from __future__ import with_statement
import sys

reserved_word = [ "program",  "var" , "if" , "else", "then", "while", "do", "for", "begin", "end", "integer", "real", "read", "write", "ident", "repeat", "writeln", "nomep", "readln", "until"];

is_in_comment = False;

symbol_msg = {
	":": " - simbolo de dois pontos", 
	"=": " - simbolo de igual",
	";": " - simbolo de ponto e virgula",
	",": " - simbolo de virgula",
	"(": " - simbolo de abre parenteses",
	")": " - simbolo de fecha parenteses",
	">": " - simbolo de maior que",
	">=": " - simbolo de maior igual que",
	"<": " - simbolo de menor que",
	"<=": " - simbolo de menor igual que",
	"+": " - simbolo de mais",
	"-": " - simbolo de menos",
	"/": " - simbolo de divisao",
	"*": " - simbolo de multiplicacao",
	"!": " - simbolo de not",
	"%": " - simbolo de porcento"
}

#funcoes de suporte
def check_token (in_word):
	global is_in_comment
	if (not is_in_comment):
		if (in_word[0] == "{"):
			is_in_comment = True
		elif (in_word in reserved_word): #procura da lista de palavras reservadas
			print (in_word + ' - Palavra reservada')
		elif (len(in_word) > 15):
			print ("Token muito grande")
		else:
			#procura no dicionario de simbolos
			print(in_word)
	elif (in_word[-1] == "}"):
		is_in_comment = False

#Arquivo a ser testado e lido
for param in sys.argv :
	if(param != "analisador.py"):
		try:
			with open(param) as in_file:
				for line in in_file:
					for word in line.split():
						check_token (word)
		except EnvironmentError:
			 print 'Arquivo nao encontrado, lendo proximo' 