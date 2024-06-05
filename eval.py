import random

class ArithEval:

    symbols = {}

    operators = {
        "+": lambda args: args[0] + args[1],
        "-": lambda args: args[0] - args[1],
        "*": lambda args: args[0] * args[1],
        "/": lambda args: args[0] // args[1],  # divisão inteira
        "seq": lambda args: args[-1],  # para sequência de instruções, retorna o último valor
        "atr": lambda args: ArithEval._attrib(args),  # atribuição de valor a uma variável
        "esc": lambda args: print(args[0]),  # função de saída (print)
        "concat": lambda args: str(args[0]) + str(args[1]),  # concatenação de strings ou listas
    }

    @staticmethod
    def _attrib(args):
        value = args[1]
        ArithEval.symbols[args[0]] = value
        return value

    @staticmethod
    def evaluate(ast):
        if type(ast) is int:
            return ast
        if type(ast) is str:
            return ArithEval.symbols.get(ast, ast)
        if type(ast) is tuple:
            if ast[0] == 'write':
                return ArithEval._eval_write(ast)
            else:
                return ArithEval._eval_tuple(ast)
        if type(ast) is list:
            return ast
        raise Exception(f"Unknown AST type: {type(ast)}")

    @staticmethod
    def _eval_write(ast):
        expr = ArithEval.evaluate(ast[1])
        if isinstance(expr, str):
            expr = ArithEval._interpolate(expr)
        ArithEval.operators['esc']([expr])
        return expr

    @staticmethod
    def _eval_tuple(ast):
        if ast[0] == 'assign':
            var_name = ast[1]
            value = ArithEval.evaluate(ast[2])
            ArithEval.symbols[var_name] = value
            return value
        elif ast[0] == 'op':
            op = ast[1]
            left = ArithEval.evaluate(ast[2])
            right = ArithEval.evaluate(ast[3])
            return ArithEval.operators[op]([left, right])
        elif ast[0] == 'concat':
            left = ArithEval.evaluate(ast[1])
            right = ArithEval.evaluate(ast[2])
            return ArithEval.operators['concat']([left, right])
        elif ast[0] == 'num':
            return ast[1]
        elif ast[0] == 'var':
            return ArithEval.symbols[ast[1]]
        elif ast[0] == 'string':
            return ast[1]
        elif ast[0] == 'list':
            return ast[1]
        elif ast[0] == 'entrada':
            return ArithEval._eval_entrada()
        elif ast[0] == 'aleatorio':
            max_value = ArithEval.evaluate(ast[1])
            return ArithEval._eval_aleatorio(max_value)
        raise Exception(f"Unknown AST tuple type: {ast[0]}")

    @staticmethod
    def _eval_entrada():
        return int(input("Digite um valor: "))

    @staticmethod
    def _eval_aleatorio(max_value):
        return random.randint(0, max_value)

    @staticmethod
    def _interpolate(string):
        import re
        def replacer(match):
            var_name = match.group(1)
            return str(ArithEval.symbols.get(var_name, ''))
        return re.sub(r'\#\{(\w+)\}', replacer, string)
