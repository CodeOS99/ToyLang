from enum import Enum

class TokenType(Enum):
    # Tokens for the lexer
    T_STRING = 3
    T_NUM = 2

    T_PLUS = 4
    T_MINUS = 5
    T_MULTIPLY = 6
    T_DIVIDE = 7
    T_MODULO = 8
    T_AND = 12
    T_OR = 13
    T_XOR = 15
    T_NOT = 16

    T_VARIABLE = 1
    T_DEFINE = 0
    T_INIT = 17
    T_PRINT = 10
    T_PRINTL = 18

class Token:
    def __init__(self, type: TokenType, value):
        self.type = type
        self.value = value

    def __str__(self):
        return self.value
