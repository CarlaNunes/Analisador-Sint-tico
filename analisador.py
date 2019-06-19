from __future__ import with_statement
import sys
#Arquivo a ser testado e lido
for param in sys.argv :
	if(param != "analisador.py"):
		try:
			with open(param) as in_file:
				print in_file.readlines()
		except EnvironmentError:
			 print 'Arquivo nao encontrado, lendo proximo' 