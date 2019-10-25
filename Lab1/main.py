from ProgramInternalForm import ProgramInternalForm
from Scanner import token_generator, is_identifier, is_constant, is_numeric_constant
from SymbolTable import SymbolTable
from Utils import *

if __name__ == '__main__':
    fileName = 'first.txt'
    file = open(fileName, 'r')
    lines = file.readlines()
    # for line in lines:
    #     print(line)

    symbolTableConstants = SymbolTable()
    symbolTableIdentifiers = SymbolTable()
    pif = ProgramInternalForm()

    counter = 0
    for line in lines:
        counter += 1
        tokens = token_generator(line[0:-1], separators)
        i = 0
        while i in range(len(tokens)):
            if tokens[i] in everything:
                if tokens[i] != ' ' and tokens[i] != '-':
                    pif.add(codification[tokens[i]], -1)
                    i += 1
                elif tokens[i] == '-' and is_numeric_constant(tokens[i+1]) and tokens[i-1] in everything:
                    pos = symbolTableConstants.find(tokens[i]+tokens[i+1])
                    if pos is None:
                        pos = symbolTableConstants.insert(tokens[i]+tokens[i+1])
                    pif.add(codification['constant'], pos)
                    i += 2
                elif tokens[i] == ' ':
                    i += 1
                else:
                    pif.add(codification[tokens[i]], -1)
                    i += 1

            elif is_identifier(tokens[i]):
                pos = symbolTableIdentifiers.find(tokens[i])
                if pos is None:
                    pos = symbolTableIdentifiers.insert(tokens[i])
                pif.add(codification['identifier'], pos)
                i += 1
            elif is_constant(tokens[i]):
                pos = symbolTableConstants.find(tokens[i])
                if pos is None:
                    pos = symbolTableConstants.insert(tokens[i])
                pif.add(codification['constant'], pos)
                i += 1
            else:
                raise Exception('Unknown token ' + tokens[i] + ' at line ' + str(counter))

    print(pif)
    print(symbolTableIdentifiers)
    print(symbolTableConstants)
    print('\n\nCodification table: ')
    for e in codification:
        print(e, " -> ", codification[e])
