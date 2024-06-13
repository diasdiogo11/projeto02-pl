from grammar import ArithGrammar
from eval import ArithEval
from pprint import PrettyPrinter

pp = PrettyPrinter(sort_dicts=False)

lg = ArithGrammar()
lg.build()


def process_input(input_string):
    try:
        ast = lg.parse(input_string)
        resultado = ArithEval.evaluate(ast)
        print(f"<< {resultado}")
    except Exception as e:
        print(e)


print("Bem-vindo ao interpretador aritmético. Comece a inserir as suas expressões ou comandos:")

while True:
    expr = input(">> ")
    if expr == "":
        break
    process_input(expr)
