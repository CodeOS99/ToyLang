from interpreter import Interpreter
from lexer import Lexer


class Runner:
    def __init__(self):
        self.interpreter = Interpreter([""])

    def run(self, prog:str):
        self.interpreter.tokens = self.lex(prog)
        self.interpret()

    def lex(self, prog: str):
        lexer = Lexer(prog)
        try:
            lexer.lex()
            # for token in lexer.tokens:
            #     print(token.value)
            return lexer.tokens
        except Exception as e:
            print(e)
        return []

    def interpret(self):
        try:
            self.interpreter.interpret()
        except Exception as e:
            print(e)

"""
[This is a sample program in this language] [This is a comment!]
[It
can
also
be
multiline!]

DEFINE howToDefineVariable "this is how you define a variable!" [this is how you define a variable]
DEFINE a 10
DEFINE b 100
INIT c [No value, only initialized]
+ a b c [Add a, b, to c]
PRINT "c is" " " [prints a string, ending with ' ']
PRINT c "\n" [prints a number c, ending with \n]

"""
