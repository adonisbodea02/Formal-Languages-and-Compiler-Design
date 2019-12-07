from Grammar import Grammar
from configuration import Configuration
from state import State


def getNextProduction(prod, listProd):
    for i in range(len(listProd)):
        if prod == listProd[i] and i < len(listProd) - 1:
            return listProd[i + 1]
    return None


### Work Stack - scoti si pui la final
### Input Stack - scoti si pui la inceput
def parser(g: Grammar, sequence):
    config = Configuration(g.S)
    while config.state != State.FINAL and config.state != State.ERROR:
        if config.state == State.NORMAL:
            if len(config.inputStack) == 0 and config.index == len(sequence):
                config.state = State.FINAL
            elif len(config.inputStack) == 0:
                config.state = State.ERROR
            else:
                if config.inputStack[0] in g.N:
                    nonTerminal = config.inputStack[0]
                    firstProduction = g.get_productions_for_non_terminal(nonTerminal)[0]
                    config.workStack.append(firstProduction)
                    config.inputStack = firstProduction[1] + config.inputStack[1:]
                else:
                    if config.index == len(sequence):
                        config.state = State.BACK
                    elif config.inputStack[0] == 'e':
                        config.workStack.append('e')
                        config.inputStack = config.inputStack[1:]
                    elif config.inputStack[0] == sequence[config.index]:
                        config.index += 1
                        config.workStack.append(config.inputStack[0])
                        config.inputStack = config.inputStack[1:]
                    else:
                        config.state = State.BACK
        else:
            if config.state == State.BACK:
                if config.workStack[-1] in g.E:
                    if config.workStack[-1]=='e':
                        config.workStack.pop(-1)
                    else:
                        config.index -= 1
                        terminal = config.workStack.pop(-1)
                        config.inputStack = [terminal] + config.inputStack
                else:
                    lastProduction = config.workStack[-1]
                    productions = g.get_productions_for_non_terminal(lastProduction[0])
                    nextProd = getNextProduction(lastProduction, productions)
                    if nextProd:
                        config.state = State.NORMAL
                        config.workStack.pop(-1)
                        config.workStack.append(nextProd)
                        config.inputStack = config.inputStack[len(lastProduction[1]):]
                        config.inputStack = nextProd[1] + config.inputStack
                    elif config.index == 0 and lastProduction[0] == g.S:
                        config.state = State.ERROR
                    else:
                        config.workStack.pop(-1)
                        if lastProduction[1] == ['e']:
                            config.inputStack = [lastProduction[0]] + config.inputStack
                        else:
                            config.inputStack = [lastProduction[0]] + config.inputStack[len(lastProduction[1]):]
    if config.state == State.ERROR:
        print("Error")
    else:
        for prod in config.workStack:
            if prod in g.P:
                print(prod)


g = Grammar.read_from_file('input.txt')
input = ['2', '4', '11', '12', '15', '30', '1', '17', '16']
# input='aacbc'
f = open("in.txt", "r")
input = f.readline().split()
parser(g, input)
