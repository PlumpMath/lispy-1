from core import cons, EmptyList, BinOp
from outhput_handler import show, eval_lisp


def test():
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

    assert show(l1) == '(1 2)', 'l1 Not passed'
    assert show(l2) == '(1 ())', 'l2 Not passed'
    assert show(l3) == '((1 2) (3 4))', 'l3 Not passed'
    assert show(l4) == '(1 (2 ()))', 'l4 Not passed'
    assert show(l5) == '(+ (7 (4 ())))', 'l5 Not passed'

    assert eval_lisp(l6) == 3, 'l6 Not passed'
    assert eval_lisp(l7) == 28, 'l7 Not passed'
    assert eval_lisp(l8) == 5, 'l8 Not passed'
    assert eval_lisp(l9) == 3, 'l9 Not passed'

    assert eval_lisp(l10) == 50, 'l10 Not passed'

    print('all tests passed')

test()


