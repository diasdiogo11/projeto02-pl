from grammar import ArithGrammar
from eval import ArithEval
from pprint import PrettyPrinter

pp = PrettyPrinter(sort_dicts=False)

ag = ArithGrammar()

# Sequência de instruções
exemplos = [
    "tmp_01 = 2*3+4 ;",
    "a1_ = 20 - (3 * 5) ;",
    "idade_valida? = 1;",
    "mult_3! = a1_ * 3 ;"
]

# Avaliar as instruções
for frase in exemplos:
    print(f"----------------------")
    print(f"--- frase '{frase}'")
    ast = ag.parse(frase)
    print("AST:")
    pp.pprint(ast)
    result = ArithEval.evaluate(ast)
    print("Resultado da avaliação:", result)

# Mostrar o valor da última instrução avaliada
final_result = ArithEval.evaluate(ast)
print("Resultado final:", final_result)