from tokens import TokenType


class Interpreter:
    def __init__(self, tokens, repl=False):
        self.repl = repl
        self.variables = {}
        self.line_to_idx = {}
        self.tokenHis = [tokens]
        self.run_num = 0
        self.curr_idx = 0
        self.curr_token = self.tokenHis[self.run_num][0] if tokens else None

    def build_line_table(self):
        self.line_to_idx.clear()
        for run_num, tokens in enumerate(self.tokenHis):
            for idx, token in enumerate(tokens):
                if token.type == TokenType.T_LINE_NUM:
                    line_num = token.value
                    self.line_to_idx[line_num] = (run_num, idx + 1)

    def interpret(self):
        if self.repl:
            if self.run_num < len(self.tokenHis) - 1:
                self.run_num += 1
            else:
                self.tokenHis.append(self.tokenHis[self.run_num])
                self.run_num = len(self.tokenHis) - 1
        else:
            self.run_num = 0

        self.curr_idx = 0
        self.curr_token = self.tokenHis[self.run_num][0]
        self.build_line_table()

        while self.curr_token is not None:
            match self.curr_token.type:
                case TokenType.T_DEFINE:
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

                case TokenType.T_PLUS | TokenType.T_MINUS | TokenType.T_MULTIPLY | TokenType.T_DIVIDE | TokenType.T_MODULO | TokenType.T_AND | TokenType.T_OR | TokenType.T_XOR | TokenType.T_NOT | TokenType.T_E | TokenType.T_GE | TokenType.T_LE | TokenType.T_L | TokenType.T_G:
                    op = self.curr_token.value
                    self.go_ahead()
                    o1 = self.get_value()
                    self.go_ahead()
                    o2 = self.get_value()
                    self.go_ahead()
                    self.set_variable(self.curr_token.value, str(eval(o1 + op + o2)), False)

                case TokenType.T_INIT:
                    self.go_ahead()
                    name = self.curr_token.value
                    self.set_variable(name, 0, True)

                case TokenType.T_LINE_NUM:
                    self.go_ahead()
                    continue

                case TokenType.T_JL | TokenType.T_JLE | TokenType.T_JG | TokenType.T_JGE | TokenType.T_JE | TokenType.T_JNE:
                    op = self.curr_token.value
                    self.go_ahead()
                    o1 = self.get_value()
                    self.go_ahead()
                    o2 = self.get_value()
                    self.go_ahead()
                    target_line = self.get_value()
                    if eval(o1 + op + o2):
                        self.jump_to(target_line)
                        continue

                case TokenType.T_J:
                    self.go_ahead()
                    self.jump_to(self.get_value())
                    continue

            self.go_ahead()

    def go_ahead(self):
        self.curr_idx += 1
        if self.curr_idx < len(self.tokenHis[self.run_num]):
            self.curr_token = self.tokenHis[self.run_num][self.curr_idx]
        else:
            self.curr_token = None

    def get_value(self):
        if self.curr_token.type == TokenType.T_VARIABLE:
            return self.get_variable(self.curr_token.value)
        return self.curr_token.value

    def get_variable(self, name):
        if name not in self.variables:
            raise Exception(f"Undefined variable {name}")
        return self.variables[name]

    def set_variable(self, name, val, can_be_uninitialized):
        if name not in self.variables and not can_be_uninitialized:
            raise Exception(f"Undefined variable {name}")
        self.variables[name] = val

    def jump_to(self, target_line):
        if target_line not in self.line_to_idx:
            raise Exception(f"Unknown line number {target_line}")
        run_num, idx = self.line_to_idx[target_line]
        self.run_num = run_num
        self.curr_idx = idx
        self.curr_token = self.tokenHis[run_num][idx]
