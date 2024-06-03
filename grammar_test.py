# arith_grammar04.py
from grammar import ArithGrammar
from pprint import PrettyPrinter

pp = PrettyPrinter(sort_dicts=False)

ag = ArithGrammar()

exemplos = [  # exemplos a avaliar de forma independente...
    "tmp_01 = 2*3+4 ;",
    "a1_ = 12345 - (5191 * 15) ;",
    "idade_valida? = 1;",
    "mult_3! = a1_ * 3 ;"
]

for frase in exemplos:
    print(f"----------------------")
    print(f"--- frase '{frase}'")
    res = ag.parse(frase)
    print("resultado: ")
    pp.pprint(res)
