from typing import final
from tokens import Token, TokenType

class Lexer:
    def __init__(self, text):
        self.text = text
        self.curr_idx = 0
        self.tokens = []

    def lex(self):
        while self.curr_idx < len(self.text):
            # strings
            if self.text[self.curr_idx] == "\"":
                s = ""
                self.curr_idx += 1
                while self.curr() != "\"":
                    if self.curr() == '\0':
                        raise Exception("Close your strings!")
                    s += self.curr()
                    self.curr_idx += 1
                self.curr_idx += 1
                self.tokens.append(Token(TokenType.T_STRING, s))

            # numbers
            elif self.text[self.curr_idx].isnumeric():
                initIdx: int = self.curr_idx
                can_have_point = True
                while True:
                    n = self.next()
                    if n.isnumeric():
                        self.curr_idx += 1
                    elif n == '.':
                        if can_have_point:
                            self.curr_idx += 1
                            can_have_point = False
                        else:
                            raise Exception("Multiple decimal points!")
                    else:
                        break
                self.curr_idx += 1
                self.tokens.append(Token(TokenType.T_NUM, self.text[initIdx:self.curr_idx]))

            elif self.text[self.curr_idx] == "+":
                self.tokens.append(Token(TokenType.T_PLUS, "+"))
                self.curr_idx += 1
            elif self.text[self.curr_idx] == "-":
                self.tokens.append(Token(TokenType.T_MINUS, "-"))
                self.curr_idx += 1
            elif self.text[self.curr_idx] == "*":
                self.tokens.append(Token(TokenType.T_MULTIPLY, "*"))
                self.curr_idx += 1
            elif self.text[self.curr_idx] == "/":
                self.tokens.append(Token(TokenType.T_DIVIDE, "/"))
                self.curr_idx += 1
            elif self.text[self.curr_idx] == "%":
                self.tokens.append(Token(TokenType.T_MODULO, "%"))
                self.curr_idx += 1
            elif self.text[self.curr_idx] == "[":
                self.curr_idx += 1
                while True:
                    n = self.next()
                    if n == "\0":
                        raise Exception("Unclosed comment")
                    elif n == "]":
                        self.curr_idx += 2
                        break
                    self.curr_idx += 1
            else:
                if self.text[self.curr_idx] in [" ", "\n", "\t"]:
                    self.curr_idx += 1
                    continue
                initIdx = self.curr_idx
                while True:
                    n = self.next()
                    if n.isalpha():
                        self.curr_idx += 1
                    else:
                        break
                self.curr_idx += 1
                word: str = self.text[initIdx:self.curr_idx]
                match word:
                    case "AND":
                        self.tokens.append(Token(TokenType.T_AND, "and"))
                    case "XOR":
                        self.tokens.append(Token(TokenType.T_XOR, "^"))
                    case "OR":
                        self.tokens.append(Token(TokenType.T_OR, "or"))
                    case "NOT":
                        self.tokens.append(Token(TokenType.T_NOT, "not"))
                    case "DEFINE":
                        self.tokens.append(Token(TokenType.T_DEFINE, "define"))
                    case "PRINT":
                        self.tokens.append(Token(TokenType.T_PRINT, "print"))
                    case "PRINTN":
                        self.tokens.append(Token(TokenType.T_PRINTI, "printi"))
                    case _:
                        self.tokens.append(Token(TokenType.T_VARIABLE, word))

    def curr(self):
        if self.curr_idx >= len(self.text):
            return '\0'
        return self.text[self.curr_idx]

    def next(self):
        if self.curr_idx >= len(self.text) - 1:
            return '\0'
        return self.text[self.curr_idx + 1]
