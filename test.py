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

    assert show(pre1) == '(> 1 2 ())', 'pre1 Not passed!'
    assert not eval_lisp(pre1, e), 'pre1 Not Accepted!'

    print('core tests passed')


def env_test():
    e = Env()

    eval_lisp(cons(SpecialForm('def'), cons(Symbol('a'), cons(3, EmptyList()))), e)
    assert eval_lisp(cons(BinOp('*'), cons(Symbol('a'), cons(10, EmptyList()))), e) == 30, 'e1 Not passed'

    print('env tests passed')


def inp_test():
    p1 = parse('(1 2)')
    print(show(p1))
    p3 = parse('(1 2 3 4)')
    print(show(p3))
    p4 = parse('(1 2)(3 4)')
    print(show(p4))
    p5 = parse('((1 2)(3 4))')
    print(show(p5))


test_core()
env_test()
# inp_test()
