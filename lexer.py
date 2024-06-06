import ply.lex as plex

class ArithLexer:
    tokens = ("NUM", "VAR", "ESCREVER", "STRING", "CONCAT", "LIST", "ENTRADA", "ALEATORIO", "FUNCAO", "FIM", "FOLD", "MAP", "NEG")
    literals = ['+', '-', '*', '/', '(', ')', '=', ';', '[', ']', ',', ':']
    t_ignore = " \t\n"

    def __init__(self):
        self.lexer = None

    def t_NUM(self, t):
        r"[0-9]+"
        t.value = int(t.value)
        return t

    def t_ESCREVER(self, t):
        r"[Ee][Ss][Cc][Rr][Ee][Vv][Ee][Rr]"
        return t

    def t_STRING(self, t):
        r'\".*?\"'
        t.value = t.value[1:-1]
        return t

    def t_CONCAT(self, t):
        r'<>'
        return t
    
    def t_LIST(self, t):
        r'\[[0-9\s,]*\]'
        t.value = eval(t.value)  # Converte a string da lista em uma lista real de Python
        return t

    def t_ENTRADA(self, t):
        r"ENTRADA"
        return t

    def t_ALEATORIO(self, t):
        r"ALEATORIO"
        return t
    
    def t_FOLD(self, t):
        r"fold"
        return t
    
    def t_MAP(self, t):
        r"map"
        return t
    
    def t_VAR(self, t):
        r"[a-z_][a-zA-Z_0-9]*[\!\?]?"
        return t

    def t_comment_multiline(self, t):
        r'\{\-(.|\n)*?\-\}'
        pass

    def t_comment_singleline(self, t):
        r'\-\-.*'
        pass

    def t_FUNCAO(self, t):
        r"FUNCAO"
        return t
    
    def t_FIM(self, t):
        r"FIM"
        return t
    
    def t_NEG(self, t):
        r"NEG"
        return t

    def t_error(self, t):
        print(f"Unexpected token: [{t.value[:10]}]")
        exit(1)
    
    def build(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)

    def input(self, string):
        self.lexer.input(string)

    def token(self):
        token = self.lexer.token()
        return token if token is None else token.type 
