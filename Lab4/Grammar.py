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
        string = string.split('=')[1]
        string = string.replace('\n', '')
        string = string.replace('}', '')
        string = string.replace('{', '')
        string=string.split(',')
        return  string

    @staticmethod
    def get_symbols_from_console(string):
        symbols = []
        for i in range(0, len(string)):
            if string[i].isalpha():
                symbols.append(string[i])
        return symbols

    @staticmethod
    def read_from_file(filename):
        with open(filename) as f:
            line = f.readline()
            N = Grammar.get_symbols_from_file(line)

            line = f.readline()
            E = Grammar.get_symbols_from_file(line)

            line = f.readline()
            S = line.split('=')[1].replace('\n','')

            P = []
            lines = f.readlines()
            for i in range(1, len(lines) - 1):
                rule = lines[i].strip('\t').strip('\n').strip(',')
                (lhs, rhs) = rule.split('->')
                lhs = lhs.strip()
                rhs = [value.strip() for value in rhs.split('|')]
                for j in rhs:
                    P.append((lhs, j.split()))

            return Grammar(N, E, P, S)

    def get_productions_for_non_terminal(self, symbol):
        if not self.is_non_terminal(symbol):
            return "This is not a non-terminal"
        return [rule for rule in self.P if rule[0] == symbol]
