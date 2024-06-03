import ply.lex as plex

class ArithLexer:
    tokens = ("NUM", "VAR")
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

    def build(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)

    def input(self, string):
        self.lexer.input(string)

    def token(self):
        return self.lexer.token()

    def t_error(self, t):
        print(f"Unexpected token: [{t.value[:10]}]")
        exit(1)
