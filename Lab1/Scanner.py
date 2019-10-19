from Utils import *
import re


def is_identifier(token):
    return re.match('^[a-zA-Z]([a-zA-Z]|[0-9]){,7}$', token) is not None


def is_constant(token):
    return re.match('^(0|-?[1-9][0-9]*)$|^\'[a-zA-Z0-9]*\'$', token) is not None


def is_part_of_operator(char):
    for op in operators:
        if char in op:
            return True
    return False


def get_operator_token(line, index):
    token = ''

    while index < len(line) and is_part_of_operator(line[index]) and is_part_of_operator(token+line[index]):
        token += line[index]
        index += 1

    return token, index


def get_string_token(line, index):
    token = ''
    quote_count = 0

    while index < len(line) and quote_count < 2:
        if line[index] == "'":
            quote_count += 1
        token += line[index]
        index += 1

    return token, index


def token_generator(line, list_of_separators):
    token = ""
    index = 0

    while index < len(line):
        if line[index] == "'":
            if token:
                yield token
            token, index = get_string_token(line, index)
            yield token
            token = ''

        elif is_part_of_operator(line[index]):
            if token:
                yield token
            token, index = get_operator_token(line, index)
            yield token
            token = ''

        elif line[index] in list_of_separators:
            if token:
                yield token
            token, index = line[index], index + 1
            yield token
            token = ''

        else:
            token += line[index]
            index += 1

    if token:
        yield token


# print([token for token in token_generator('(a+bra&&ca/2<=+a>=b||2)', separators)])
