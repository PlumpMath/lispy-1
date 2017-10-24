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

    assert show(l1) == '(1 2)', 'l1 Not passed'
    assert show(l2) == '(1 ())', 'l2 Not passed'
    assert show(l3) == '((1 2) (3 4))', 'l3 Not passed'
    assert show(l4) == '(1 (2 ()))', 'l4 Not passed'
    assert show(l5) == '(+ (7 (4 ())))', 'l5 Not passed'

    assert eval_lisp(l6) == 3, 'l6 Not passed'
    assert eval_lisp(l7) == 28, 'l7 Not passed'

test()


