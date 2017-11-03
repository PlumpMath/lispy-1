from core import is_empty, car, cdr, get_type, get_value, get_env, set_env, def_env, sub_env, Lambda, cons
from input_handler import parse


def show(l, start_of_list=True):
    type = get_type(l)
    new_list = True

    if type == 'ConsList':
        if is_empty(l):
            return '()'
        if get_type(car(l)) != 'ConsList':
            new_list = False
        if start_of_list:
            return "({} {})".format(show(car(l)), show(cdr(l), new_list))
        else:
            return "{} {}".format(show(car(l)), show(cdr(l), False))
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
        raise Exception('Wtf is this bin operator???')

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


def realize_pred_op(op, l, r):
    result = False
    if op == '<':
        result = l < r
    elif op == '<=':
        result = l <= r
    elif op == '>':
        result = l >= r
    elif op == '==':
        result = l == r
    elif op == '!=':
        result = l != r
    elif op == 'and':
        result = l and r
    elif op == 'or':
        result = l or r
    else:
        raise Exception('Wtf is this pred operator???')

    return result


def eval_pred_op(h, l, e):
    if is_empty(l):
        return None

    left_operand = eval_lisp(car(l), e)
    l = cdr(l)
    result = True
    while not is_empty(l):
        right_operand = eval_lisp(car(l), e)
        result = result and realize_pred_op(get_value(h), left_operand, right_operand)
        if not result:
            return False
        left_operand = right_operand
        l = cdr(l)
    return True


def eval_special_form(h, l, e):
    if is_empty(l):
        return None
    val = get_value(h)
    if val == 'def':
        t = get_type(car(l))
        if t != 'Symbol':
            raise Exception('Cant assign to {}. Symbol required.'.format(t))
        k = get_value(car(l))
        v = eval_lisp(car(cdr(l)), e)
        def_env(e, k, v)
    elif val == 'defn':
        name = car(l)
        args = car(cdr(l))
        body = car(cdr(cdr(l)))
        k = get_value(name)
        lmbd = Lambda(args, body, e)
        def_env(e, k, lmbd)
    elif val == 'lambda':
        args = car(l)
        body = cdr(l)
        return Lambda(args, body, e)
    elif val == 'if':
        pred = eval_lisp(car(l), e)
        t = car(cdr(l))
        f = car(cdr(cdr(l)))
        if pred:
            return eval_lisp(t, e)
        else:
            return eval_lisp(f, e)
    elif val == 'car':
        h = car(l)
        return eval_lisp(car(eval_lisp(h, e)), e)
    elif val == 'cdr':
        return cdr(eval_lisp(car(l), e))
    elif val == 'cons':
        h = eval_lisp(car(l), e)
        t = eval_lisp(car(cdr(l)), e)
        return cons(h, t)
    elif val == '`':
        return car(l)
    return 'OK'


def eval_lambda(head_form, args, e):
    su = sub_env(head_form.env)
    sub_args = head_form.args
    while not is_empty(sub_args):
        if is_empty(args):
            raise Exception('not enough args!')
        arg = eval_lisp(car(args), e)
        k = eval_lisp(car(sub_args), su)
        def_env(su, k, arg)
        sub_args = cdr(sub_args)
        args = cdr(args)
    body = head_form.body
    return eval_lisp(body, su)


def eval_symbol(s, e):
    t = get_type(s)
    if t != 'Symbol':
        raise Exception('{} is not a Symbol'.format(t))
    return get_env(e, s)


def eval_lisp(l, e):
    type = get_type(l)

    if type == 'ConsList':
        if is_empty(l):
            return l
        head_form = eval_lisp(car(l), e)
        head_form_type = get_type(head_form)
        if head_form_type == 'BinOp':
            return eval_bin_op(head_form, cdr(l), e)
        if head_form_type == 'PredOp':
            return eval_pred_op(head_form, cdr(l), e)
        if head_form_type == 'SpecialForm':
            return eval_special_form(head_form, cdr(l), e)
        if head_form_type == 'Symbol':
            return eval_symbol(head_form, e)
        if head_form_type == 'Lambda':
            return eval_lambda(head_form, cdr(l), e)
        return head_form
    if type == 'Symbol':
        if get_value(l) == 'None':
            return None
        return eval_symbol(l, e)
    return l
