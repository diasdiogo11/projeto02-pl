import ply.lex as plex

class ArithLexer:
    tokens = ("NUM", "VAR", "ESCREVER", "STRING")
    literals = ['+', '-', '*', '/', '(', ')', '=', ';']
    t_ignore = " \t\n"

    def __init__(self):
        self.lexer = None

    def t_NUM(self, t):
        r"[0-9]+"
        t.value = int(t.value)
        return t

    def t_VAR(self, t):
        r"[a-z_][a-zA-Z_0-9]*[\!\?]?"
        return t

    def t_ESCREVER(self, t):
        r"[Ee][Ss][Cc][Rr][Ee][Vv][Ee][Rr]"
        t.type = 'ESCREVER'  # Define o tipo do token como 'ESCREVER'
        return t
    
    def t_STRING(self, t):
        r'\".*?\"'
        t.value = t.value[1:-1]
        return t

    def build(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)

    def input(self, string):
        self.lexer.input(string)

    def token(self):
        return self.lexer.token()

    def t_error(self, t):
        print(f"Unexpected token: [{t.value[:10]}]")
        exit(1)
