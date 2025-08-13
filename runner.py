from lexer import Lexer


class Runner:
    def run(self, prog:str):
        self.lex(prog)

    def lex(self, prog: str):
        lexer = Lexer(prog)
        try:
            lexer.lex()
            for token in lexer.tokens:
                print(token.value)
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
DEFINE c [No initialized value]
+ a b c [Add a, b, to c]
PRINT "c is" [prints a string]
PRINTN c "\n" [prints a number c, ending with \n]

"""
