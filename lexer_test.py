# arith_lexer_test.py
from lexer import ArithLexer

exemplos = [
    """lista = [ 1, 2, 3 ] ;
	ESCREVER( lista );
	vazia = [] ; """
]

for frase in exemplos:
    print(f"----------------------")
    print(f"frase: '{frase}'")
    al = ArithLexer()
    al.build()
    al.input(frase)
    print("tokens: ", end="")
    while True:
        tk = al.token()
        if not tk:
            break
        print(tk, end="")
    print()
