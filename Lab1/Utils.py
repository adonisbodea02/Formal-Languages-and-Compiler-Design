separators = ['[', ']', '{', '}', '(', ')', ';', ' ']
operators = ['+', '-', '*', '/', '%', '<', '<=', '=', '>=', '>',
             '==', '&&', '||', '!', '!=']
reservedWords = ['char', 'int', 'if', 'else', 'printf', 'scanf', 'while', 'main', 'return']

everything = reservedWords + operators + separators
codification = dict([(everything[i], i + 2) for i in range(len(everything))])
codification['identifier'] = 0
codification['constant'] = 1
