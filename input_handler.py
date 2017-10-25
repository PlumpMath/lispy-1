from core import cons, Symbol, EmptyList


def check_brackets(string):
    stack = []
    for i in string:
        if i is '(':
            stack.append(i)

        if i is ')':
            if len(stack) == 0:
                return False

            stack.pop()

    if len(stack) == 0:
        return True

    return False


def pinch_block(string):
    stack = []
    result = 0

    for i in string:
        result += 1

        if i is '(':
            stack.append(i)

        if i is ')':
            if len(stack) == 0:
                raise Exception('Wrong input!')

            stack.pop()
            if len(stack) == 0:
                return result
    return -1


def find_cdr(string):
    br_stack = []
    for i, val in enumerate(string):
        if val == '(':
            br_stack.append(val)
        if val == ')':
            if len(br_stack) == 0:
                return -1
            br_stack.pop()
        if val == ' ' and (len(br_stack) == 1 or len(br_stack) == 0):
            return i
    return -1


def trim_brackets(string):
    return string[1:-1]


def get_tok(tok):
    if tok.isalpha():
        return tok
    elif tok.isnumeric():
        return int(tok)


def tokenize(string):
    if len(string) == 0:
        return EmptyList()
    elif string[0] == '(':
        pinch_ind = pinch_block(string)
        if pinch_ind == len(string):
            cdr_ind = find_cdr(string)
            car_tok = parse(string[1:cdr_ind])
            cdr_tok = parse(string[cdr_ind + 1:])
            return cons(car_tok, cdr_tok)
        else:
            car_tok = parse(string[:pinch_ind])
            cdr_tok = parse(string[pinch_ind + 1:])
            return cons(car_tok, cdr_tok)
    else:
        cdr_ind = find_cdr(string)
        if cdr_ind == -1:
            end = False
            if string[-1] == ')':
                string = string[:-1]
                end = True
            car_tok = get_tok(string)
            if end:
                return cons(car_tok, EmptyList())
            return car_tok
        else:
            car_tok = get_tok(string[:cdr_ind])
            return cons(car_tok, parse(string[cdr_ind + 1:]))


def fix_spaces(string):
    result = ''
    fix = False
    for i in string:
        if i is ')':
            fix = True
        elif fix and i is '(':
            fix = False
            result += ' '
        else:
            fix = False
        result += i
    return result


def parse(string):
    return tokenize(fix_spaces(string))
