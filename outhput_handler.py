from core import is_empty, car, cdr, get_type, get_value


def show(l):
    type = get_type(l)

    if type == 'ConsList':
        if is_empty(l):
            return '()'
        return "({} {})".format(show(car(l)), show(cdr(l)))
    return get_value(l)


def realize_bin_op(op, l, r):
    result = 0
    if op == '+':
        result = l + r
    elif op == '-':
        result = l - r
    elif op == '*':
        result = l * r
    elif op == '/':
        result = l / r
    elif op == '%':
        result = l % r
    else:
        raise Exception('Wtf is this operator???')

    return result


def eval_bin_op(h, l):
    if is_empty(l):
        return None
    result = eval_lisp(car(l))
    l = cdr(l)
    while not is_empty(l):
        right_operand = eval_lisp(car(l))
        result = realize_bin_op(get_value(h), result, right_operand)
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
