from interperter.BasicExecute import BasicExecute
from interperter.BasicLexer import BasicLexer
from interperter.BasicParser import BasicParser

if __name__ == '__main__':
    lexer = BasicLexer()
    parser = BasicParser()
    print('+---------------------------+')
    print('+         Yoshi 1.0         +')
    print('+---------------------------+')
    env = {}

    while True:

        try:
            text = input('Yoshi-1.0 > ')

            with open(text) as file:
                file = file.read()

        except EOFError:
            break

        if file:
            tree = parser.parse(lexer.tokenize(text))
            BasicExecute(tree, env)