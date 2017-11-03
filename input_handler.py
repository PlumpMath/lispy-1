from core import cons, Symbol, EmptyList, BinOp, PredOp, SpecialForm

bin_ops = {'+', '-', '*', '/', '%'}
pred_ops = {'<', '<=', '>', '>=', '==', '!=', 'and', 'or'}
spec_forms = {'car', 'cdr', 'cons', 'def', 'defn', 'if', 'lambda', '`', 'cond'}


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
    return -1


def trim_brackets(string):
    return string[1:-1]


def tokenize(string):
    if string.isnumeric():
        return int(string)
    elif string in bin_ops:
        return BinOp(string)
    elif string in pred_ops:
        return PredOp(string)
    elif string in spec_forms:
        return SpecialForm(string)
    elif string[0] == '"':
        return string
    elif string[0] == '`':
        return string[1:]
    elif string[0].isalpha():
        return Symbol(string)
    else:
        return float(string)


def parse(string, level=0):
    string = string.strip()
    length = len(string)
    if length == 0:
        return EmptyList()
    if string[0] == '(':
        pinch_ind = pinch_block(string)
        if length == pinch_ind:
            if level == 0:
                return parse(string[1:-1], level=1)
            else:
                car_tok = parse(string[1:-1], level + 1)
                return cons(car_tok, EmptyList())
        else:
            cdr_ind = find_cdr(string)
            car_tok = parse(string[1:cdr_ind - 1], level + 1)
            cdr_tok = parse(string[cdr_ind:], level=level)
            return cons(car_tok, cdr_tok)
    else:
        cdr_ind = find_cdr(string)
        if cdr_ind != -1:
            car_tok = tokenize(string[:cdr_ind])
            cdr_tok = parse(string[cdr_ind:], level)
            return cons(car_tok, cdr_tok)
        else:
            car_tok = tokenize(string)
            cdr_tok = EmptyList()
            return cons(car_tok, cdr_tok)
