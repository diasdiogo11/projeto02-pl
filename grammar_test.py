# arith_grammar04.py
from grammar import ArithGrammar
from pprint import PrettyPrinter

pp = PrettyPrinter(sort_dicts=False)

ag = ArithGrammar()
ag.build()

exemplos = [
    "FUNCAO soma(a,b),: a+b ;"
]

for frase in exemplos:
    print(f"----------------------")
    print(f"--- Frase '{frase}'")
    res = ag.parse(frase)
    print("Resultado: ")
    pp.pprint(res)
