class FiniteAutomaton:

    def __init__(self, Q, E, delta, q0, F):
        self.Q = Q
        self.E = E
        self.delta = delta
        self.q0 = q0
        self.F = F

    def is_state(self, value):
        return value in self.Q

    @staticmethod
    def get_states_from_file(line):
        states = []
        for i in range(1, len(line)-1):
            if line[i] == 'q':
                states.append(line[i:i+2])
        return states

    @staticmethod
    def get_states_from_console(line):
        states = []
        for i in range(0, len(line) - 1):
            if line[i] == 'q':
                states.append(line[i:i + 2])
        return states

    @staticmethod
    def get_symbols_from_file(line):
        symbols = []
        for i in range(1, len(line)):
            if line[i].isalpha() or line[i].isnumeric():
                symbols.append(line[i])
        return symbols

    @staticmethod
    def get_symbols_from_console(line):
        symbols = []
        for i in range(0, len(line)):
            if line[i].isalpha() or line[i].isnumeric():
                symbols.append(line[i])
        return symbols

    @staticmethod
    def read_from_console():
        line = input("Give the set of states: ")
        Q = FiniteAutomaton.get_states_from_console(line)

        line = input("Give the alphabet: ")
        E = FiniteAutomaton.get_symbols_from_console(line)

        line = input("Give the starting state: ")
        q0 = FiniteAutomaton.get_states_from_console(line)[0]

        line = input("Give the final states: ")
        F = FiniteAutomaton.get_states_from_console(line)

        delta = []
        ok = True
        while ok:
            transition = input("Give me a transition: (press 0 to stop) ")
            if transition is '0':
                ok = False
            if ok:
                transition = transition.strip()
                (lhs, rhs) = transition.split('->')
                lhs = lhs.split(',')
                for j in range(len(lhs)):
                    lhs[j] = lhs[j].strip().strip('(').strip(')').strip()
                rhs = rhs.strip()
                delta.append((lhs, rhs))

        return FiniteAutomaton(Q, E, q0, delta, F)

    @staticmethod
    def read_from_file(filename):
        with open(filename) as f:
            line = f.readline()
            Q = FiniteAutomaton.get_states_from_file(line)

            line = f.readline()
            E = FiniteAutomaton.get_symbols_from_file(line)

            line = f.readline()
            q0 = FiniteAutomaton.get_states_from_file(line)[0]

            line = f.readline()
            F = FiniteAutomaton.get_states_from_file(line)

            delta = []
            lines = f.readlines()
            for i in range(1, len(lines) - 1):
                transition = lines[i].strip('\t').strip('\n')
                (lhs, rhs) = transition.split('->')
                lhs = lhs.split(',')
                for j in range(len(lhs)):
                    lhs[j] = lhs[j].strip().strip('(').strip(')').strip()
                rhs = rhs.strip().strip(',')
                delta.append((lhs, rhs))

            return FiniteAutomaton(Q, E, delta, q0, F)

    @staticmethod
    def from_regular_grammar(rg):
        if not rg.is_regular:
            return "This is not a regular grammar"
        Q = rg.N + ['K']
        E = rg.E
        q0 = rg.S
        F = ['K']

        delta = []

        for production in rg.P:
            state2 = 'K'
            state1, rhs = production
            if state1 == q0[0] and rhs[0] == 'e':
                F.append(q0[0])
                state2 = q0

            symbol = rhs[0]

            if len(rhs) == 2:
                state2 = rhs[1]
                if rhs[1] == q0[0] and rhs[1] not in F:
                    F.append(q0[0])

            delta.append(((state1, symbol), state2))

        return FiniteAutomaton(Q, E, delta, q0, F)
