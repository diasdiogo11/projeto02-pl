# arith_grammar04.py
from grammar import ArithGrammar
from pprint import PrettyPrinter

pp = PrettyPrinter(sort_dicts=False)

ag = ArithGrammar()
ag.build()

exemplos = [
    'lista =[1,2,3] ;'
]

for frase in exemplos:
    print(f"----------------------")
    print(f"--- frase '{frase}'")
    res = ag.parse ( frase ) 
    print("resultado: ")
    pp.pprint(res)
