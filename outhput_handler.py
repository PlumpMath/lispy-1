from core import is_empty, cons, car, cdr, ConsList, EmptyList, get_type, get_value, BinOp


def show(l):
    type = get_type(l)

    if type == 'ConsList':
        if is_empty(l):
            return '()'
        return "({} {})".format(show(car(l)), show(cdr(l)))
    return get_value(l)


def eval_bin_op(h, l):
    if is_empty(l):
        return None
    result = eval_lisp(car(l))
    l = cdr(l)
    while not is_empty(l):
        right_operand = eval_lisp(car(l))

        if get_value(h) == '+':
            result += right_operand
        if get_value(h) == '-':
            result -= right_operand
        if get_value(h) == '*':
            result *= right_operand
        if get_value(h) == '/':
            result /= right_operand
        if get_value(h) == '%':
            result %= right_operand

        l = cdr(l)
    return result


def eval_lisp(l):
    type = get_type(l)

    if type == 'ConsList':
        if is_empty(l):
            return l
        head_form = eval_lisp(car(l))
        head_form_type = get_type(head_form)
        if head_form_type == 'BinOp':
            return eval_bin_op(head_form, cdr(l))
        return head_form
    return l
