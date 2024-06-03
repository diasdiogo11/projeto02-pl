import ply.yacc as pyacc
from lexer import ArithLexer

class ArithGrammar:
    tokens = ArithLexer.tokens

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
    )

    def __init__(self):
        self.lexer = ArithLexer()
        self.lexer.build()
        self.parser = pyacc.yacc(module=self)

    def parse(self, data):
        return self.parser.parse(data, lexer=self.lexer.lexer)

    def p_statement_assign(self, p):
        'statement : VAR "=" expression ";"'
        p[0] = ('assign', p[1], p[3])

    def p_statement_expr(self, p):
        'statement : expression ";"'
        p[0] = ('expr', p[1])

    def p_expression_binop(self, p):
        '''expression : expression '+' expression
                      | expression '-' expression
                      | expression '*' expression
                      | expression '/' expression'''
        p[0] = ('binop', p[2], p[1], p[3])

    def p_expression_group(self, p):
        'expression : "(" expression ")"'
        p[0] = p[2]

    def p_expression_num(self, p):
        'expression : NUM'
        p[0] = ('num', p[1])

    def p_expression_var(self, p):
        'expression : VAR'
        p[0] = ('var', p[1])

    def p_error(self, p):
        print(f"Syntax error at '{p.value}'" if p else "Syntax error at end of input")
