from core import is_empty, car, cdr, get_type, get_value, get_env, set_env, def_env


def show(l):
    type = get_type(l)

    if type == 'ConsList':
        if is_empty(l):
            return '()'
        return "({} {})".format(show(car(l)), show(cdr(l)))
    if type == "<class 'str'>":
        return '"{}"'.format(l)
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


def eval_bin_op(h, l, e):
    if is_empty(l):
        return None
    result = eval_lisp(car(l), e)
    l = cdr(l)
    while not is_empty(l):
        right_operand = eval_lisp(car(l), e)
        result = realize_bin_op(get_value(h), result, right_operand)
        l = cdr(l)
    return result


def eval_special_form(h, l, e):
    if is_empty(l):
        return None

    if get_value(h) == 'def':
        k = eval_lisp(car(l), e)
        v = eval_lisp(cdr(l), e)
        def_env(e, k, v)


def eval_lisp(l, e):
    type = get_type(l)

    if type == 'ConsList':
        if is_empty(l):
            return l
        head_form = eval_lisp(car(l), e)
        head_form_type = get_type(head_form)
        if head_form_type == 'BinOp':
            return eval_bin_op(head_form, cdr(l), e)
        if head_form_type == 'SpecialForm':
            return eval_special_form(head_form, cdr(l), e)
        if head_form_type == 'Symbol':
            return get_env(e, head_form)
        return head_form
    if type == 'Symbol':
        return get_env(e, l)
    return l
