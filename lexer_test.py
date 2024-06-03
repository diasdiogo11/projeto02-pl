# arith_lexer_test.py
from lexer import ArithLexer

exemplos = [ # exemplos a avaliar de forma independente... 
           "tmp_01 = 2*3+4 ;"
"a1_ = 12345 - (5191 * 15) ;"
"idade_valida? = 1;"
"mult_3! = a1_ * 3 ;"""]


for frase in exemplos:
	print(f"----------------------")
	print(f"frase: '{frase}'")
	al = ArithLexer()
	al.build()
	al.input(frase)
	print('tokens: ',end="")
	while True:
		tk = al.token() 
		if not tk: 
			break
		print(tk,end="")
	print()	