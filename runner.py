from interpreter import Interpreter
from lexer import Lexer
from tokens import TokenType, Token


class Runner:
    def __init__(self, repl=False):
        self.repl = repl
        self.interpreter = Interpreter([], repl=repl)

    def run(self, prog: str, is_file=False):
        tokens = self.lex(prog)
        if not tokens:
            return
        if self.repl:
            self.interpreter.tokenHis.append(tokens)
            self.interpreter.run_num = len(self.interpreter.tokenHis) - 1
            self.interpreter.curr_idx = 0
            self.interpreter.tokens = tokens
        else:
            self.interpreter.tokenHis = [tokens]
            self.interpreter.run_num = 0
            self.interpreter.curr_idx = 0
            self.interpreter.tokens = tokens
        self.interpret()

    def lex(self, prog: str):
        lexer = Lexer(prog)
        try:
            lexer.lex()
            return lexer.tokens
        except Exception as e:
            print(e)
        return []

    def interpret(self):
        try:
            self.interpreter.interpret()
        except Exception as e:
            print(e)
