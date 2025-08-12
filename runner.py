from lexer import Lexer


class Runner:
    def run(self, prog:str):
        self.lex(prog)

    def lex(self, prog: str):
        lexer = Lexer(prog)
        try:
            lexer.lex()
        except Exception as e:
            print(e)

"""
[This is a sample program in this language] [This is a comment!]
[It
can
also
be
multiline!]

define how_to_define_variable "this is how you define a variable!" [this is how you define a variable]
define a 10
define b 100
define c [No initialized value]
+ a b c [Add a, b, to c]
print c [prints c]
"""
