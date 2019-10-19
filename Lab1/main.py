from ProgramInternalForm import ProgramInternalForm
from Scanner import token_generator, is_identifier, is_constant
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
        for token in token_generator(line[0:-1], separators):
            if token in everything:
                pif.add(codification[token], -1)
            elif is_identifier(token):
                pos = symbolTableIdentifiers.find(token)
                if pos is None:
                    pos = symbolTableIdentifiers.insert(token)
                pif.add(codification['identifier'], pos)
            elif is_constant(token):
                pos = symbolTableConstants.find(token)
                if pos is None:
                    pos = symbolTableConstants.insert(token)
                pif.add(codification['constant'], pos)
            else:
                raise Exception('Unknown token ' + token + ' at line ' + str(counter))

    print(pif)
    print(symbolTableIdentifiers)
    print(symbolTableConstants)
    print('\n\nCodification table: ')
    for e in codification:
        print(e, " -> ", codification[e])
