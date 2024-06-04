# eval.py
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
        raise Exception(f"Unknown AST type: {type(ast)}")

    @staticmethod
    def _eval_write(ast):
        expr = ArithEval.evaluate(ast[1])
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
        elif ast[0] == 'num':
            return ast[1]
        elif ast[0] == 'var':
            return ArithEval.symbols[ast[1]]
        raise Exception(f"Unknown AST tuple type: {ast[0]}")