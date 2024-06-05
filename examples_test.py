from lexer import ArithLexer
from grammar import ArithGrammar
from eval import ArithEval

# Crie as instâncias do lexer, parser e avaliador
lexer = ArithLexer()
lexer.build()
parser = ArithGrammar()
parser.build()
evaluator = ArithEval()

# Ler o script do arquivo
with open('examples.txt', 'r') as file:
    script = file.read()

# Parse e execute o script linha a linha
for line in script.split('\n'):
    if line.strip():  # Ignora linhas vazias
        try:
            ast = parser.parse(line)
            if ast:  # Verifica se o AST foi gerado corretamente
                result = evaluator.evaluate(ast)
                if result is not None:
                    print(result)
        except Exception as e:
            print(f"Erro ao processar a linha: {line}")
            print(e)
