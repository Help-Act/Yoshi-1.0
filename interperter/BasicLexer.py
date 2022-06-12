from sly import Lexer


class BasicLexer(Lexer):
    # Set of token names.   This is always required
    tokens = {NUMBER, LPAREN, RPAREN, STRING, VAR, ID, WHILE, ALSO, CHECK, DOC,
              RAWR, PLUS, MINUS, TIMES, DIVIDE, ASSIGN, CBS, CBE, TYPE, NUMCON,
              BOOL, LIBREQ, COMMA, EQ, LT, LE, GT, GE, NE}

    literals = {'(', ')', '{', '}', ';', ','}

    # String containing ignored characters
    ignore = ' \t'

    # Regular expression rules for tokens
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    LPAREN = r'\('
    RPAREN = r'\)'
    COMMA = r','
    CBS  = r'\{'
    CBE = r'\}'
    EQ = r'=='
    ASSIGN = r'='
    LE = r'<='
    LT = r'<'
    GE = r'>='
    GT = r'>'
    NE = r'!='

    #@_(r'\"[a-zA-Z_]*\"')
    #def STRING(self, string):
    #    string.value = str(string.value)
    #    return string
    #

    STRING = r'\"[a-zA-Z0-9_]*\"'


    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    # Identifiers and keywords
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['check'] = CHECK
    ID['also'] = ALSO
    ID['while'] = WHILE
    ID['doc'] = DOC
    ID['rawr'] = RAWR
    ID['leaf'] = VAR
    ID['type'] = TYPE
    ID['num'] = NUMCON
    ID['true'] = BOOL
    ID['false'] = BOOL
    ID['gather'] = LIBREQ

    ignore_multi_comment = r'~~$ [a-zA-Z_][a-zA-Z0-9_] ~~$.*'
    #ignore_single_comment = r'[.*'

    #Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
       self.lineno += t.value.count('\n')

    def error(self, t):
      print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
      self.index += 1

if __name__ == '__main__':
    text = input('calc > ')
    with open(text) as file:
        text = file.read()
        print(text)

    lexer = BasicLexer()
    for tok in lexer.tokenize(text):
        print(tok)
