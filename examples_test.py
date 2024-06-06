import sys
from lexer import ArithLexer
from grammar import ArithGrammar
from eval import ArithEval

# Verifica se o nome do arquivo foi passado como argumento na linha de comando
if len(sys.argv) != 2:
    print("Usage: python script.py filename.fca")
    sys.exit(1)

# Obtém o nome do arquivo a partir da linha de comando
filename = sys.argv[1]

# Crie as instâncias do lexer, parser e avaliador
lexer = ArithLexer()
lexer.build()
parser = ArithGrammar()
parser.build()
evaluator = ArithEval()

# Ler o script do arquivo
try:
    with open(filename, 'r') as file:
        script = file.read()
except FileNotFoundError:
    print(f"Arquivo {filename} não encontrado.")
    sys.exit(1)

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
