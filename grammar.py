import ply.yacc as pyacc
from lexer import ArithLexer

class ArithGrammar:
    tokens = ArithLexer.tokens

    precedence = (
        ('left', '+', '-', 'CONCAT'),
        ('left', '*', '/'),
    )

    def __init__(self):
        self.yacc = None
        self.lexer = None
        self.tokens = None

    def build(self, **kwargs):
        self.lexer = ArithLexer()
        self.lexer.build(**kwargs)
        self.tokens = self.lexer.tokens
        self.yacc = pyacc.yacc(module=self, **kwargs)

    def parse(self, string):
        self.lexer.input(string)
        return self.yacc.parse(lexer=self.lexer.lexer)
    
    # Regra de produção para o ponto de entrada do parser
    def p_start(self, p):
        """start : statement
                 | expression"""
        p[0] = p[1]

    def p_statement_assign(self, p):
        'statement : VAR "=" expression ";"'
        p[0] = ('assign', p[1], p[3])

    def p_statement_expr(self, p):
        'statement : expression ";"'
        p[0] = ('expr', p[1])
    
    def p_statement_write(self, p):
        '''statement : ESCREVER "(" expression ")" ";"
                     | ESCREVER "(" STRING ")" ";"
                     | ESCREVER "(" VAR ")" ";"'''
        p[0] = ('write', p[3])

    def p_expression_binop(self, p):
        '''expression : expression '+' expression
                      | expression '-' expression
                      | expression '*' expression
                      | expression '/' expression'''
        p[0] = ('op', p[2], p[1], p[3])
    
    def p_expression_concat(self, p):
        'expression : expression CONCAT expression'
        p[0] = ('concat', p[1], p[3])

    def p_expression_group(self, p):
        'expression : "(" expression ")"'
        p[0] = p[2]

    def p_expression_num(self, p):
        'expression : NUM'
        p[0] = ('num', p[1])

    def p_expression_var(self, p):
        'expression : VAR'
        p[0] = ('var', p[1])

    def p_expression_string(self, p):
        'expression : STRING'
        p[0] = ('string', p[1])

    def p_expression_list(self, p):
        'expression : LIST'
        p[0] = ('list', p[1])

    def p_expression_entrada(self, p):
        'expression : ENTRADA "(" ")"'
        p[0] = ('entrada',)

    def p_expression_aleatorio(self, p):
        '''expression : ALEATORIO "(" NUM ")"
                      | ALEATORIO "(" VAR ")"'''
        p[0] = ('aleatorio', p[3])

    def p_expression_function(self, p):
        'expression : FUNCAO VAR "(" params ")" "," ":" expression ";"'
        p[0] = ('function', p[2], p[4], p[8])

    def p_params(self, p):
        '''params : VAR
                  | VAR "," params'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3]

    def p_expression_func_call(self, p):
        'expression : VAR "(" arguments ")"'
        p[0] = ('func_call', p[1], p[3])

    def p_arguments(self, p):
        '''arguments : expression
                     | expression "," arguments'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3]

    def p_error(self, p):
        print(f"Syntax error at '{p.value}'" if p else "Syntax error at end of input")
