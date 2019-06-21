from __future__ import with_statement
import sys

reserved_word = [ "program",  "var" , "if" , "else", "then", "while", "do", "for", "begin", "end", "integer", "real", "read", "write", "ident", "repeat", "writeln", "nomep", "readln", "until"];

is_in_comment = False;

symbol_msg = {
	">=": " - simbolo de maior igual que",
	"<=": " - simbolo de menor igual que",
	":": " - simbolo de dois pontos", 
	";": " - simbolo de ponto e virgula",
	",": " - simbolo de virgula",
	"(": " - simbolo de abre parenteses",
	")": " - simbolo de fecha parenteses",
	">": " - simbolo de maior que",
	"<": " - simbolo de menor que",
	"=": " - simbolo de igual",
	"+": " - simbolo de mais",
	"-": " - simbolo de menos",
	"/": " - simbolo de divisao",
	"*": " - simbolo de multiplicacao",
	"!": " - simbolo de not",
	"%": " - simbolo de porcento"
}

identifier_msg = {
	"integer;": " - identificador eh integer",
	"real;": " - identificador eh real",
	"digit;": " - identificador eh digit",
	"lalg;": " - identificador eh nome do programa"
}

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def fragment_sub_tokens (in_word): #tira expressoes
	for sub_sy in symbol_msg:
		symb_pos = in_word.find(sub_sy)
		if symb_pos == 0:  #eh apenas o simbolo
			if len(sub_sy) == len(in_word):
				return [ 0, in_word, 0]
			else:
				return [ 0, sub_sy, in_word[symb_pos+len(sub_sy): len(in_word)]]
	for sub_sy in symbol_msg:
		symb_pos = in_word.find(sub_sy)		
		if symb_pos > 0:
			return [ in_word[0:symb_pos], sub_sy, in_word[symb_pos+len(sub_sy): len(in_word)]]
		# el
	for sub_sy in symbol_msg:
		symb_pos = in_word.find(sub_sy)
		if symb_pos == -1:  #nao achou nada
			return [ in_word, 0, 0]


#funcoes de suporte
def check_token (in_word):
	global is_in_comment
	tk_list = fragment_sub_tokens(in_word)
	if (not is_in_comment):
		if (in_word == "\n") or (in_word == ""): 
			return
		if ("{" in in_word):
			if(in_word.find("{") > 0) :
				check_token(in_word[0: in_word.find("{")])
			is_in_comment = True
			if ("}" in in_word):
				is_in_comment = False
				check_token(in_word[in_word.find("}")+1: -1])
		elif (in_word in reserved_word): #procura da lista de palavras reservadas
			print (in_word + ' - Palavra reservada')
		elif tk_list[0] == 0 and tk_list[2] == 0:
			print (tk_list[1] + symbol_msg[tk_list[1]])
		elif tk_list[1] == 0 and tk_list[2] == 0:
			if tk_list[0].isalpha():
				print (tk_list[0] + ' - id') #nomes de id
			else:
				if("." in tk_list[0]):
					first_tk = tk_list[0]
					dot_pos = first_tk.find(".")
					dot_pre = first_tk[0:dot_pos]
					dot_post = first_tk[dot_pos+1:len(first_tk)]
					if (dot_pre in reserved_word):
						print (dot_pre + ' - Palavra reservada')
					if(is_number(dot_pre) and is_number(dot_post)):
						print (first_tk + ' - id')
				else:
					print (tk_list[0] + ' - id malformado')

		elif tk_list[1] != 0 and tk_list[2] != 0:
			#procura no dicionario de simbolos
			first_tk = tk_list[0]
			if(first_tk != 0):
				if tk_list[1] == ";":
					if (first_tk + ";" in identifier_msg): #identificadores
						print (first_tk + identifier_msg[first_tk+";"])
						return
					else:
						print (first_tk + " - ERRO - identificador nao encontrado")
						return
				if (len(first_tk) > 15):
					print ("Token muito grande")
				else:
					if("." in first_tk):
						dot_pos = first_tk.find(".")
						dot_pre = first_tk[0:dot_pos]
						dot_post = first_tk[dot_pos+1: len(first_tk)]
						if(is_number(dot_pre) and is_number(dot_post)):
							print (first_tk + ' - id')
						else:
							print (first_tk + ' - id malformado')
					else:
						print (first_tk + ' - id')
			if(tk_list[1] != 0):
				print (tk_list[1] + symbol_msg[tk_list[1]])
			if(tk_list[2] != 0):
				if (len(tk_list[2]) > 15):
					print ("Token muito grande")
				elif (tk_list[2] != '') :
					check_token(tk_list[2])
	elif ("}" in in_word):
		if(in_word.find("}") < len(in_word) - 1):
			is_in_comment = False
			check_token(in_word[in_word.find("}")+1: -1])
		else:
			is_in_comment = False

#Arquivo a ser testado e lido
for param in sys.argv :
	if(param != "analisador.py"):
		try:
			with open(param) as in_file:
				linin = "----------------------------------------------------------\n"
				print (linin + "Abrindo arquivo: " + param + "\n" + linin)
				for line in in_file:
					for word in line.split():
						check_token (word)
		except EnvironmentError:
			 print 'Arquivo nao encontrado, lendo proximo' 