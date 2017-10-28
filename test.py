from core import cons, EmptyList, BinOp, Env, set_env, get_env, SpecialForm, Symbol, PredOp
from input_handler import parse
from outhput_handler import show, eval_lisp


def test_core():
    e = Env()

    l1 = cons(1, 2)
    l2 = cons(1, EmptyList())
    l3 = cons(cons(1, 2), cons(3, 4))
    l4 = cons(1, cons(2, EmptyList()))
    l5 = cons(BinOp('+'), cons(7, cons(4, EmptyList())))
    l6 = cons(BinOp('-'), cons(7, cons(4, EmptyList())))
    l7 = cons(BinOp('*'), cons(7, cons(4, EmptyList())))
    l8 = cons(BinOp('/'), cons(10, cons(2, EmptyList())))
    l9 = cons(BinOp('%'), cons(7, cons(4, EmptyList())))

    l10 = cons(BinOp('*'), cons(10, cons(cons(BinOp('+'), cons(2, cons(3, EmptyList()))), EmptyList())))

    l11 = cons(SpecialForm('def'), cons(Symbol('a'), cons(3, EmptyList())))
    l12 = cons(SpecialForm('def'), cons(Symbol('a'), cons('asd', EmptyList())))

    l13 = cons(1, cons(cons(1, cons(2, EmptyList())), EmptyList()))
    print(show(l13))

    l14 = cons(BinOp('+'), cons(cons(BinOp('+'), cons(2, cons(3, EmptyList()))), cons(3, EmptyList())))
    print('l14', show(l14))

    assert show(l1) == '(1 2)', 'l1 Not passed'
    assert show(l2) == '(1 ())', 'l2 Not passed'
    assert show(l3) == '((1 2) (3 4))', 'l3 Not passed'
    assert show(l4) == '(1 2 ())', 'l4 Not passed'
    assert show(l5) == '(+ 7 4 ())', 'l5 Not passed'

    assert eval_lisp(l6, e) == 3, 'l6 Not passed'
    assert eval_lisp(l7, e) == 28, 'l7 Not passed'
    assert eval_lisp(l8, e) == 5, 'l8 Not passed'
    assert eval_lisp(l9, e) == 3, 'l9 Not passed'

    assert eval_lisp(l10, e) == 50, 'l10 Not passed'

    assert show(l11) == '(def a 3 ())', 'l11 Not passed'
    assert show(l12) == '(def a "asd" ())', 'l12 Not passed'

    pre1 = cons(PredOp('>'), cons(1, cons(2, EmptyList())))
    pre2 = cons(PredOp('>'), cons(1, cons(2, cons(3, EmptyList()))))
    pre3 = cons(PredOp('>'), cons(2, cons(1, cons(3, EmptyList()))))

    assert show(pre1) == '(> 1 2 ())', 'pre1 Not passed!'
    assert not eval_lisp(pre1, e), 'pre1 Not Accepted!'

    assert show(pre2) == '(> 1 2 3 ())', 'pre2 Not passed!'
    assert not eval_lisp(pre2, e), 'pre2 Not Accepted!'

    assert show(pre3) == '(> 2 1 3 ())', 'pre3 Not passed!'
    assert not eval_lisp(pre3, e), 'pre3 Not Accepted!'

    print('core tests passed')


def env_test():
    e = Env()

    eval_lisp(cons(SpecialForm('def'), cons(Symbol('a'), cons(3, EmptyList()))), e)
    assert eval_lisp(cons(BinOp('*'), cons(Symbol('a'), cons(10, EmptyList()))), e) == 30, 'e1 Not passed'

    print('env tests passed')


def inp_test():
    e = Env()
    p1 = parse('1 2')
    print(show(p1))
    p1 = parse('(1 2)')
    print(show(p1))
    p1 = parse('(+ 1 2)')
    print(show(p1))
    p1 = parse('(1 2 3 4)')
    print(show(p1))
    p1 = parse('(+ (+ 3 2) 3)')
    print(eval_lisp(p1, e))
    print(show(p1))
    p1 = parse('(1 (4 5))')
    print(show(p1))
    p1 = parse('(1 2) (3 4) (5 6)')
    print(show(p1))

    p1 = parse('((def a 10) (+ 1 a))')
    print(eval_lisp(p1, e))

    p1 = parse('(def a (lambda (x) (* x x)))')
    print(show(p1))


def test_lambda():
    e = Env()
    l1 = cons(SpecialForm('def'), cons(Symbol('a'), cons(
        cons(SpecialForm('lambda'),
             cons(cons(Symbol('x'), EmptyList()), cons(cons(BinOp('*'), cons(Symbol('x'), cons(Symbol('x'), EmptyList()))), EmptyList())))
        , EmptyList())))

    l2 = cons(Symbol('a'), cons(10, EmptyList()))
    print(eval_lisp(l1, e))
    print(eval_lisp(l2, e))


# test_lambda()
# test_core()
# env_test()
# inp_test()


# (* a (+ (+ 1 2) 2) (+ 2 (+ 1 2)))
# (def a 10)
e = Env()
print('go')
n = input()
while len(n) != 0:
    print(eval_lisp(parse(n), e))
    n = input()

