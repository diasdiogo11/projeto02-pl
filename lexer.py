import ply.lex as plex

class ArithLexer:
    tokens = ("NUM", "VAR", "ESCREVER", "STRING", "CONCAT", "LIST")
    literals = ['+', '-', '*', '/', '(', ')', '=', ';', '[', ']']
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
        t.type = 'ESCREVER'
        return t

    def t_STRING(self, t):
        r'\".*?\"'
        t.value = t.value[1:-1]
        return t

    def t_CONCAT(self, t):
        r'<>'
        t.type = 'CONCAT'
        return t
    
    def t_LIST(self, t):
        r'\[.*?\]'
        t.value = eval(t.value)  # Converte a string da lista em uma lista real de Python
        return t

    def t_comment_multiline(self, t):
        r'\{\-(.|\n)*?\-\}'
        pass

    def t_comment_singleline(self, t):
        r'\-\-.*'
        pass

    def t_error(self, t):
        print(f"Unexpected token: [{t.value[:10]}]")
        exit(1)
    
    def build(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)

    def input(self, string):
        self.lexer.input(string)

    def token(self):
        return self.lexer.token()
