from Grammar import Grammar
from FiniteAutomaton import FiniteAutomaton


def print_menu():
    print("1. Grammar")
    print("2. Finite automaton")
    print("0. Exit")


def print_grammar_menu():
    print("1. Read grammar from file")
    print("2. Read grammar from console")
    print("3. See the non-terminals of the grammar")
    print("4. See the terminals of the grammar")
    print("5. See the set of productions of the grammar")
    print("6. See the starting symbol of the grammar")
    print("7. See the set of productions for a given non-terminal of the grammar")
    print("8. Check if the grammar is regular")
    print("9. Construct the finite automaton from the given grammar")
    print("0. Back")
    print("If none of the first 2 options was chosen, the default grammar is read from the file 'grammar1.txt'")


def print_fa_menu():
    print("1. Read finite automaton from file")
    print("2. Read finite automaton from console")
    print("3. See the set of states of the finite automaton")
    print("4. See the alphabet of the finite automaton")
    print("5. See the set of transitions of the finite automaton")
    print("6. See the initial state of the finite automaton")
    print("7. See the set of final states of the finite automaton")
    print("8. Construct the regular grammar from the given finite automaton")
    print("0. Back")
    print("If none of the first 2 options was chosen, the default finite automaton is read from the file 'fa1.txt'")


def main_menu():
    g = Grammar.read_from_file("grammar1.txt")
    fa = FiniteAutomaton.read_from_file("fa1.txt")
    print_menu()
    option = input("Choose a option: ")
    if option == '1':
        grammar_menu(g)
    elif option == '2':
        fa_menu(fa)
    elif option == '0':
        return
    else:
        print("No such option")
        main_menu()


def grammar_menu(g):
    print_grammar_menu()
    option = input("Choose a option: ")
    if option == '1':
        filename = input("Give the filename: ")
        g = Grammar.read_from_file(filename)
        grammar_menu(g)
    elif option == '2':
        g = Grammar.read_from_console()
        grammar_menu(g)
    elif option == '3':
        print(g.N)
        grammar_menu(g)
    elif option == '4':
        print(g.E)
        grammar_menu(g)
    elif option == '5':
        for rule in g.P:
            print(rule[0] + " -> " + rule[1])
        grammar_menu(g)
    elif option == '6':
        print(g.S)
        grammar_menu(g)
    elif option == '7':
        symbol = input("Give the symbol: ")
        result = g.get_productions_for_non_terminal(symbol)
        if isinstance(result, list):
            for rule in result:
                print(rule[0] + " -> " + rule[1])
        else:
            print(result)
        grammar_menu(g)
    elif option == '8':
        print(g.is_regular())
        grammar_menu(g)
    elif option == '9':
        fa = FiniteAutomaton.from_regular_grammar(g)
        if isinstance(fa, FiniteAutomaton):
            print("Set of states")
            print(fa.Q)
            print("Alphabet")
            print(fa.E)
            print("Set of transitions")
            for transition in fa.delta:
                print('(' + transition[0][0] + ", " + transition[0][1] + ") -> " + transition[1])
            print("Initial state")
            print(fa.q0)
            print("Set of final states")
            print(fa.F)
        else:
            print(fa)
        grammar_menu(g)
    elif option == '0':
        main_menu()
    else:
        print("No such option")
        grammar_menu(g)


def fa_menu(fa):
    print_fa_menu()
    option = input("Choose a option: ")
    if option == '1':
        filename = input("Give the filename: ")
        fa = FiniteAutomaton.read_from_file(filename)
        fa_menu(fa)
    elif option == '2':
        fa = FiniteAutomaton.read_from_console()
        fa_menu(fa)
    elif option == '3':
        print(fa.Q)
        fa_menu(fa)
    elif option == '4':
        print(fa.E)
        fa_menu(fa)
    elif option == '5':
        for transition in fa.delta:
            print('(' + transition[0][0] + ", " + transition[0][1] + ") -> " + transition[1])
        fa_menu(fa)
    elif option == '6':
        print(fa.q0)
        fa_menu(fa)
    elif option == '7':
        print(fa.F)
        fa_menu(fa)
    elif option == '8':
        g = Grammar.from_finite_automaton(fa)
        print("Set of non-terminal symbols")
        print(g.N)
        print("Set of terminal symbols")
        print(g.E)
        print("Set of productions")
        for rule in g.P:
            print(rule[0] + " -> " + rule[1])
        print("Starting symbol")
        print(g.S)
        fa_menu(fa)
    elif option == '0':
        main_menu()
    else:
        print("No such option")
        fa_menu(fa)


main_menu()
