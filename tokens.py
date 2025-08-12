from enum import Enum

class TokenType(Enum):
    # Tokens for the lexer
    T_DEFINE = 0
    T_VARIABLE = 1
    T_NUM = 2
    T_STRING = 3
    T_PLUS = 4
    T_MINUS = 5
    T_MULTIPLY = 6
    T_DIVIDE = 7
    T_MODULO = 8
    T_LPAREN = 9
    T_PRINT = 10

class Token:
    def __init__(self, type: TokenType, value):
        self.type = type
        self.value = value

    def __str__(self):
        return self.value
