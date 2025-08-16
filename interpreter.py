from tokens import TokenType


class Interpreter:
    def __init__(self, tokens):
        self.tokens = tokens
        self.curr_idx = 0
        self.curr_token = self.tokens[self.curr_idx]
        self.variables = {}

    def interpret(self):
        self.curr_idx = 0
        self.curr_token = self.tokens[self.curr_idx]

        match self.curr_token.type:
            case TokenType.T_DEFINE: # DEFINE var_name var_value
                self.go_ahead()
                if self.curr_token.type != TokenType.T_VARIABLE:
                    raise Exception("Expected variable name after DEFINE")

                name = self.curr_token.value
                self.go_ahead()
                self.set_variable(name, self.get_value(), True)

            case TokenType.T_PRINT:
                self.go_ahead()
                val = self.get_value()
                self.go_ahead()
                end = self.get_value().encode("utf-8").decode("unicode_escape")
                print(val, end=end)

            case TokenType.T_PRINTL:
                self.go_ahead()
                val = self.get_value()
                print(val)

            case TokenType.T_PLUS | TokenType.T_MINUS | TokenType.T_MULTIPLY | TokenType.T_DIVIDE | TokenType.T_MODULO | TokenType.T_AND | TokenType.T_OR | TokenType.T_XOR | TokenType.T_NOT:
                    op = self.curr_token.value
                    self.go_ahead()
                    o1 = self.get_value()
                    self.go_ahead()
                    o2 = self.get_value()
                    self.go_ahead()
                    self.set_variable(self.curr_token.value, str(eval(o1 + op + o2)),False)

            case TokenType.T_INIT:
                self.go_ahead()
                name = self.curr_token.value
                self.set_variable(name, 0, True)

    def go_ahead(self):
        self.curr_idx += 1
        if self.curr_idx < len(self.tokens):
            self.curr_token = self.tokens[self.curr_idx]
        else:
            self.curr_token = None

    def get_value(self):
        if self.curr_token.type == TokenType.T_VARIABLE:
            return self.get_variable(self.curr_token.value)
        return self.curr_token.value

    def get_variable(self, name):
        if not (name in self.variables):
            raise Exception(f"Undefined variable {name}")
        return self.variables[name]

    def set_variable(self, name, val, can_be_uninitialized):
        if not (name in self.variables) and (not can_be_uninitialized):
            raise Exception(f"Undefined variable {name}")
        self.variables[name] = val
        print(self.variables)
