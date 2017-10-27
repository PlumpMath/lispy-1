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
    in_inner_block = 0
    in_string = 0

    for i, val in enumerate(string):
        if val == '(':
            in_inner_block += 1
        if val == ')':
            in_inner_block -= 1
        if val == ' ' and in_inner_block <= 0:
            return i

    # br_stack = []
    # for i, val in enumerate(string):
    #     if val == '(':
    #         br_stack.append(val)
    #     if val == ')':
    #         if len(br_stack) == 0:
    #             return -1
    #         br_stack.pop()
    #     if val == ' ' and (len(br_stack) == 1 or len(br_stack) == 0):
    #         return i
    return -1


def trim_brackets(string):
    return string[1:-1]


def tokenize(string):
    return string


def parse(string):
    string = string.strip()
    if len(string) == 0:
        return EmptyList()
    elif string[0] == '(':
        pinch_ind = pinch_block(string)
        if pinch_ind == len(string):
            return parse(string[1:-1])
        else:
            cdr_ind = find_cdr(string)
            car_tok = parse(string[:cdr_ind])
            cdr_tok = parse(string[cdr_ind:])
            return cons(car_tok, cdr_tok)
    else:
        cdr_ind = find_cdr(string)
        if cdr_ind != -1:
            car_tok = tokenize(string[:cdr_ind])
            cdr_tok = parse(string[cdr_ind:])
            return cons(car_tok, cdr_tok)
        else:
            car_tok = tokenize(string)
            cdr_tok = EmptyList()
            return cons(car_tok, cdr_tok)

