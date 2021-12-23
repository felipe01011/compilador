#importe de galerias 
import ply.lex as lex
import re
import codecs
import os
import sys
#Definicion de las palabras reservadas 
reservadas = ['BEGIN', 'END', 'IF', 'THEN', 'WHILE', 'DO', 'CALL', 'CONST',
		'VAR', 'PROCEDURE', 'OUT', 'IN', 'ELSE'
		]
#Definicion de tokens
tokens = reservadas+['ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
		'ODD', 'ASSIGN', 'NE', 'LT', 'LTE', 'GT', 'GTE',
		'LPARENT', 'RPARENT', 'COMMA', 'SEMMICOLOM','PROCEDURE','DOT', 'UPDATE']

# reservadas = {
	# 'begin':'BEGIN',
	# 'end':'END',
	# 'if':'IF',
	# 'then':'THEN',
	# 'while':'WHILE',
	# 'do':'DO',
	# 'call':'CALL',
	# 'const':'CONST',
	# 'int':'VAR',
	# 'procedure':'PROCEDURE',
	# 'out':'OUT',
	# 'in':'IN',
	# 'else':'ELSE'
# }

# tokens = tokens+list(reservadas.values())
#Lista para definir los simbolos que corresponde a cada token 
t_ignore = '\t '
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE = r':='

#Definicion de lasfunciones de los tokens especiales 
def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		# reservadas.get(t.value,'ID')
		t.type = t.value

	return t


def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

# dsfjksdlgjklsdgjsdgslxcvjlk-,.


def t_COMMENT(t):
	r'\#.*'
	pass


def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t


def t_error(t):
	print
	"caracter ilegal '%s'" % t.value[0]
	t.lexer.skip(1)

# def searchFiles(folder):
#    files = []
#    num_file = ''
#    response = False
#    res_file = None

#    for _, _, _files in os.walk(folder):
#        files = _files
#        print(*["{}. {}".format(c+1,file) for c, file in enumerate(files)] )

#    while response == False:
#        num_file = input('\nNumero de test de prueba')
#        if int(num_file) in [idx+1 for idx,_ in enumerate(files)]:
#            response = True
#            res_file = files[int(num_file)-1]
#            break
#        else:
#            print("Inserte un test valido")

#    print("Test: {}".format(res_file))
#    return res_file

# folder = 'test'
# file = searchFiles(folder)
# test = "{}/{}".format(folder, file)
# fp = codecs.open(test, "r", "utf-8")
# chain = fp.read()
# fp.close()

analizer = lex.lex()
#analizer.input(chain)

# while True:

#     tok = analizer.token()

#     if tok is None: break

#     print(tok)

