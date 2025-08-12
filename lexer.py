from tokens import Token, TokenType


class Lexer:
    def __init__(self, text):
        self.text = text
        self.curr_idx = 0
        self.tokens = []

    def lex(self):
        while self.curr_idx < len(self.text):
            if self.text[self.curr_idx] == "\"":
                s = ""
                self.curr_idx += 1
                while self.curr() != "\"":
                    s+=self.curr()
                    self.curr_idx += 1

                    if self.curr() == '\0':
                        raise Exception("Close your strings!")
                self.curr_idx += 1

                self.tokens.append(Token(TokenType.T_STRING, s))
                print(s)
            else:
                raise Exception("??? What did you write?")

    def curr(self):
        if self.curr_idx >= len(self.text):
            return '\0'
        return self.text[self.curr_idx]

    def next(self):
        if self.curr_idx >= len(self.text) - 1:
            return '\0'
        return self.text[self.curr_idx + 1]
