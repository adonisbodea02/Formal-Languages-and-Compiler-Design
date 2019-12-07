class Grammar:

    def __init__(self, N, E, P, S):
        self.N = N
        self.E = E
        self.P = P
        self.S = S

    def is_terminal(self, value):
        return value in self.E

    def is_non_terminal(self, value):
        return value in self.N

    @staticmethod
    def get_symbols_from_file(string):
        symbols = []
        for i in range(1, len(string)):
            if string[i].isalpha():
                symbols.append(string[i])
        return symbols

    @staticmethod
    def get_symbols_from_console(string):
        symbols = []
        for i in range(0, len(string)):
            if string[i].isalpha():
                symbols.append(string[i])
        return symbols

    @staticmethod
    def read_from_console():
        line = input("Give the set of non-terminals: ")
        N = Grammar.get_symbols_from_console(line)

        line = input("Give the set of terminals: ")
        E = Grammar.get_symbols_from_console(line)

        line = input("Give the starting symbol: ")
        S = Grammar.get_symbols_from_console(line)

        P = []
        ok = True
        while ok:
            rule = input("Give me a rule: (press 0 to stop) ")
            if rule is '0':
                ok = False
            if ok:
                rule = rule.strip()
                (lhs, rhs) = rule.split('->')
                lhs = lhs.strip()
                rhs = [value.strip() for value in rhs.split('|')]
                for j in rhs:
                    P.append((lhs, j))

        return Grammar(N, E, P, S)

    @staticmethod
    def read_from_file(filename):
        with open(filename) as f:
            line = f.readline()
            N = Grammar.get_symbols_from_file(line)

            line = f.readline()
            E = Grammar.get_symbols_from_file(line)

            line = f.readline()
            S = Grammar.get_symbols_from_file(line)[0]

            P = []
            lines = f.readlines()
            for i in range(1, len(lines)-1):
                rule = lines[i].strip('\t').strip('\n').strip(',')
                (lhs, rhs) = rule.split('->')
                lhs = lhs.strip()
                rhs = [value.strip() for value in rhs.split('|')]
                for j in rhs:
                    P.append((lhs, j))

            return Grammar(N, E, P, S)

    def is_regular(self):
        used_in_rhs = {}
        not_allowed_in_rhs = []
        
        for rule in self.P:
            lhs = rule[0]
            rhs = rule[1]
            has_terminal = False
            has_non_terminal = False
            if len(rhs) > 2:
                return False
            for char in rhs:
                if self.is_non_terminal(char):
                    if not (lhs == self.S and char == self.S):
                        used_in_rhs[char] = True
                    has_non_terminal = True
                elif self.is_terminal(char):
                    if has_non_terminal:
                        return False
                    has_terminal = True
                if char == 'e':
                    not_allowed_in_rhs.append(lhs)

            if has_non_terminal and not has_terminal:
                return False

        for char in not_allowed_in_rhs:
            if char in used_in_rhs:
                return False

        return True

    def get_productions_for_non_terminal(self, symbol):
        if not self.is_non_terminal(symbol):
            return "This is not a non-terminal"
        return [rule for rule in self.P if rule[0] == symbol]

    @staticmethod
    def from_finite_automaton(fa):
        N = fa.Q
        E = fa.E
        S = fa.q0
        P = []

        if fa.q0 in fa.F:
            P.append((fa.q0, 'E'))

        for transition in fa.delta:
            lhs, state2 = transition
            state1, symbol = lhs

            P.append((state1, symbol + state2))

            if state2 in fa.F:
                P.append((state1, symbol))

        return Grammar(N, E, P, S)


# g = Grammar.read_from_file("grammar1.txt")
# print(g.is_regular())
# print(g.P)
#
# # fa1 = FiniteAutomaton.read_from_file('fa1.txt')
# # g = Grammar.from_finite_automaton(fa1)
# # print(g.N)
# # print(g.E)
# # print(g.S)
# # print(g.P)
#
# fa2 = FiniteAutomaton.read_from_console()
# print(fa2.Q)
# print(fa2.E)
# print(fa2.delta)
# print(fa2.q0)
# print(fa2.F)

# g = Grammar.read_from_console()
# print(g.N)
# print(g.E)
# print(g.S)
# print(g.P)


