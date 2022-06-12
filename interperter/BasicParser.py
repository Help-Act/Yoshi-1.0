
from sly import Parser
import os

from interperter.BasicLexer import BasicLexer


class BasicParser(Parser):
    # Get the token list from the lexer (required)
    tokens = BasicLexer.tokens

    # Grammar rules and actions

    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
        ('right', 'UMINUS'),
    )

    def __init__(self):
        self.env = {}

    ## Var Assignment
    @_('VAR ID ASSIGN expr')
    def statement(self, p):
            self.vars = { }
            self.vars[p.ID] = p.expr

            vars = self.vars

            print(vars)

            return vars

    @_('VAR ID ASSIGN NUMBER')
    def statement(self, p):
        self.vars = {}
        self.vars[p.ID] = p.NUMBER

        vars = self.vars

        print(vars)

        return vars

    @_('VAR ID ASSIGN STRING')
    def statement(self, p):
        self.vars = {}
        self.vars[p.ID] = p.STRING

        vars = self.vars

        print(vars)

        return vars

    @_('expr')
    def statement(self, p):
        print(p.expr)

    @_('MINUS expr %prec UMINUS')
    def expr(p):
        return -p.expr

    ## TYPES

    @_('TYPE LPAREN STRING RPAREN')
    def expr(self, p):
        return print(type(p.STRING))

    @_('TYPE LPAREN NUMBER RPAREN')
    def expr(self, p):
        return print(type(p.NUMBER))

    ##  TYPE CASTING
    @_('NUMCON LPAREN STRING RPAREN')
    def expr(self, p):
        intf = p.STRING.replace("\"",  "")
        return int(intf)

    ## BOOL
    @_('BOOL')
    def expr(self, p):
        if p.BOOL == 'true':
            return True
        if p.BOOL == 'false':
            return False

    ## Regular Print Statements
    @_('DOC LPAREN STRING RPAREN')
    def expr(self, p):
        return print(p.STRING)

    @_('DOC LPAREN NUMBER RPAREN')
    def expr(self, p):
        return print(str(p.NUMBER))

    @_('DOC LPAREN expr RPAREN')
    def expr(self, p):
        return print(p.expr)

    @_('DOC LPAREN BOOL RPAREN')
    def expr(self, p):
        if p.BOOL == 'true':
            return print(str(True))
        elif p.BOOL == 'false':
            return print(str(False))

    @_('DOC LPAREN ID LPAREN STRING RPAREN')
    def expr(self, p):
        if p.ID == self.funcs[p.ID0[0]]:
            return print(p.RAWR + " " + p.ID0 + p.LPAREN0 + p.ID1 + p.RPAREN0 + p.CBS + "\n\t" + p.DOC + p.LPAREN1 + p.STRING + p.RPAREN1 + "\n " + p.CBE)

    @_('DOC LPAREN LIBREQ LPAREN STRING COMMA STRING RPAREN RPAREN')
    def expr(self, p):
        return print(str(os.environ['USERPROFILE']) + p.STRING0 + p.STRING1 + '.yoshi')
    ## Check Statement

    @_('CHECK LPAREN factor LT factor RPAREN')
    def expr(self, p):
        if p.factor0 < p.factor1:
            return print(str(p.factor0 < p.factor1))
        elif p.factor0 > p.factor1:
            return False

    @_('CHECK LPAREN factor LE factor RPAREN')
    def expr(self, p):
        if p.factor0 <= p.factor1:
            return print(str(p.factor0 <= p.factor1))
        elif p.factor0 >= p.factor1:
            return False

    @_('CHECK LPAREN factor GT factor RPAREN')
    def expr(self, p):
        if p.factor0 > p.factor1:
            return print(str(p.factor0 > p.factor1))
        elif p.factor0 < p.factor1:
            return False

    @_('CHECK LPAREN factor GE factor RPAREN')
    def expr(self, p):
        if p.factor0 >= p.factor1:
            return print(str(p.factor0 >= p.factor1))
        elif p.factor0 <= p.factor1:
            return False

    @_('CHECK LPAREN factor NE factor RPAREN')
    def expr(self, p):
        if p.factor0 != p.factor1:
            return print(str(p.factor0 != p.factor1))
        elif p.factor0 == p.factor1:
            return False

    @_('CHECK LPAREN factor EQ factor RPAREN DO')
    def expr(self, p):
        if p.factor0 == p.factor1:
            return print(str(p.factor0 == p.factor1))
        elif p.factor0 != p.factor1:
            return False

    @_('CHECK LPAREN BOOL EQ BOOL RPAREN')
    def expr(self, p):
        if p.BOOL0 == p.BOOL1:
            return True
        else:
            return False

    @_('CHECK LPAREN BOOL NE BOOL RPAREN')
    def expr(self, p):
        if p.BOOL0 != p.BOOL1:
            return True
        else:
            return False

    @_('ALSO CHECK LPAREN factor LT factor RPAREN')
    def expr(self, p):
        if p.factor0 < p.factor1:
            return print(p.factor0 < p.factor1)
        if p.factor0 > p.factor1:
            return False


    ## Functions
    @_('ID LPAREN ID RPAREN')
    def expr(self, p):
        return print(p.ID0 + p.LPAREN + p.ID1 + p.RPAREN)

    @_('RAWR ID LPAREN ID RPAREN')
    def expr(self, p):
        self.funcs[p.ID0]

    @_('RAWR ID LPAREN ID RPAREN CBS DOC LPAREN ID  RPAREN CBE')
    def expr(self, p):
        self.funcs = { }
        self.funcs[p.ID0] = p.ID0 + p.LPAREN0 + p.ID1 + p.RPAREN0
        self.funcs[p.ID0].name = p.ID0
        self.funcs[p.ID0].params[p.ID1] = p.ID1

        funcs = self.funcs

        print(funcs)


        return funcs

    ## Requiring Libraries
    @_('LIBREQ LPAREN STRING COMMA STRING RPAREN')
    def expr(self, p):
        if os.path.isfile(str(os.environ['USERPROFILE']) + p.STRING0 + p.STRING1 + ".yoshi"):
            with open(str(os.environ['USERPROFILE']) + p.STRING0 + p.STRING1 + '.yoshi') as f:
                f = f.read()





    ## STRINGS
    #@_('STRING')
    #def factor(self, p):
    #    return p.STRING
    ## MATH

    @_('expr PLUS term')
    def expr(self, p):
        return p.expr + p.term

    @_('expr MINUS term')
    def expr(self, p):
        return p.expr - p.term

    @_('term')
    def expr(self, p):
        return p.term

    @_('term TIMES factor')
    def term(self, p):
        return p.term * p.factor

    @_('term DIVIDE factor')
    def term(self, p):
        return p.term / p.factor

    @_('factor')
    def term(self, p):
        return p.factor

    @_('NUMBER')
    def factor(self, p):
        return p.NUMBER

    @_('LPAREN expr RPAREN')
    def factor(self, p):
        return p.expr

    ## Symbols


if __name__ == '__main__':
    lexer = BasicLexer()
    parser = BasicParser()

    while True:
        try:
            text = input('Yoshi-1.0 >~> ')
            with open(text) as file:
                file = file.read()


                result = parser.parse(lexer.tokenize(file))

                # print(text)
            # print(result)
        except EOFError:
            break