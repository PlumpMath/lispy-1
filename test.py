from core import cons, EmptyList, BinOp, Env, SpecialForm, Symbol, PredOp
from input_handler import parse
from outhput_handler import show, eval_lisp


def test_core():
    l1 = cons(1, 2)
    l2 = cons(1, EmptyList())
    l3 = cons(cons(1, 2), cons(3, 4))
    l4 = cons(1, cons(2, EmptyList()))
    l5 = cons(BinOp('+'), cons(7, cons(4, EmptyList())))
    l6 = cons(PredOp('<'), cons(1, cons(2, EmptyList())))
    l7 = cons(PredOp('>'), cons(1, cons(2, EmptyList())))
    l8 = cons(PredOp('and'), cons(True, cons(True, EmptyList())))
    l9 = cons(PredOp('and'), cons(True, cons(False, EmptyList())))
    l10 = cons(PredOp('or'), cons(False, cons(False, EmptyList())))
    l11 = cons(PredOp('or'), cons(False, cons(True, EmptyList())))
    l12 = cons(PredOp('or'), cons(True, cons(False, EmptyList())))

    l13 = cons(BinOp('*'), cons(10, cons(cons(BinOp('+'), cons(2, cons(3, EmptyList()))), EmptyList())))

    l14 = cons(SpecialForm('def'), cons(Symbol('a'), cons(3, EmptyList())))
    l15 = cons(Symbol('a'), EmptyList())
    l16 = cons(SpecialForm('def'), cons(Symbol('a'), cons('asd', EmptyList())))
    l17 = cons(Symbol('a'), EmptyList())

    l18 = cons(BinOp('+'), cons(cons(BinOp('+'), cons(2, cons(3, EmptyList()))), cons(3, EmptyList())))

    pre1 = cons(PredOp('>'), cons(1, cons(2, cons(3, EmptyList()))))
    pre2 = cons(PredOp('>'), cons(2, cons(1, cons(3, EmptyList()))))
    pre3 = cons(PredOp('and'), cons(cons(PredOp('>'), cons(6, cons(2, EmptyList()))), cons(pre1, EmptyList())))

    assert show(l1) == '(1 2)', 'l1 Not passed'
    assert show(l2) == '(1 ())', 'l2 Not passed'
    assert show(l3) == '((1 2) (3 4))', 'l3 Not passed'
    assert show(l4) == '(1 2 ())', 'l4 Not passed'
    assert show(l5) == '(+ 7 4 ())', 'l5 Not passed'
    assert show(l6) == '(< 1 2 ())', 'l6 Not passed'
    assert show(l7) == '(> 1 2 ())', 'l7 Not passed'
    assert show(l8) == '(and True True ())', 'l8 Not passed'
    assert show(l9) == '(and True False ())', 'l9 Not passed'
    assert show(l10) == '(or False False ())', 'l10 Not passed'
    assert show(l11) == '(or False True ())', 'l11 Not passed'
    assert show(l12) == '(or True False ())', 'l12 Not passed'
    assert show(l13) == '(* 10 (+ 2 3 ()) ())', 'l13 Not passed'

    assert show(l14) == '(def a 3 ())', 'l14 Not passed'
    assert show(l16) == '(def a "asd" ())', 'l16 Not passed'

    assert show(l18) == '(+ (+ 2 3 ()) 3 ())', 'l18 Not passed'

    assert show(pre1) == '(> 1 2 3 ())', 'pre1 Not passed'
    assert show(pre2) == '(> 2 1 3 ())', 'pre2 Not passed'
    assert show(pre3) == '(and (> 6 2 ()) (> 1 2 3 ()) ())', 'pre3 Not passed'

    print('show tests passed')

    e = Env()
    assert eval_lisp(l5, e) == 11, 'eval l5 not passed'
    assert eval_lisp(l6, e) == True, 'eval l6 not passed'
    assert eval_lisp(l7, e) == False, 'eval l7 not passed'
    assert eval_lisp(l8, e) == True, 'eval l8 not passed'
    assert eval_lisp(l9, e) == False, 'eval l9 not passed'
    assert eval_lisp(l10, e) == False, 'eval l10 not passed'
    assert eval_lisp(l11, e) == True, 'eval l11 not passed'
    assert eval_lisp(l12, e) == True, 'eval l12 not passed'
    assert eval_lisp(l13, e) == 50, 'eval l13 not passed'
    assert eval_lisp(l14, e) == 'OK', 'eval l14 not passed'
    assert eval_lisp(l15, e) == 3, 'eval l15 not passed'
    # assert eval_lisp(l16, e) == 'OK', 'eval l16 not passed'    если символ в окружение возвращает его значение
    # и прикрепляет новое значение к старому значению, а не к самому символу
    # assert eval_lisp(l17, e) == 'asd', 'eval l17 not passed'
    assert eval_lisp(l18, e) == 8, 'eval l18 not passed'
    assert eval_lisp(pre1, e) == False, 'eval pre1 not passed'
    assert eval_lisp(pre2, e) == False, 'eval pre2 not passed'
    assert eval_lisp(pre3, e) == False, 'eval pre3 not passed'

    print('eval tests passed')
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
             cons(cons(Symbol('x'), EmptyList()),
                  cons(cons(BinOp('*'), cons(Symbol('x'), cons(Symbol('x'), EmptyList()))), EmptyList())))
        , EmptyList())))

    l2 = cons(Symbol('a'), cons(10, EmptyList()))
    print(eval_lisp(l1, e))
    print(eval_lisp(l2, e))


def test_if():
    if1 = cons(SpecialForm('if'), cons(cons(PredOp('<'), cons(3,
                                                              cons(5, EmptyList()))), cons(cons(88, EmptyList()),
                                                                                           cons(cons(22, EmptyList()),
                                                                                                EmptyList()))))
    print(show(if1))
    print(eval_lisp(parse('(if (< 3 5) (12) (22))'), Env()))


def test_fib():
    e = Env()
    fib = parse('(def fib (lambda (n) (if (< n 2) 1 (+ (fib (- n 1)) (fib (- n 2))))))')
    print(show(fib))
    eval_lisp(fib, e)
    exec_fib = parse('(fib 30)')
    print(eval_lisp(exec_fib, e))


# test_fib()
# test_lambda()
test_core()
env_test()
# inp_test()
# test_if()


# (* a (+ (+ 1 2) 2) (+ 2 (+ 1 2)))
# (def a 10)
# e = Env()
# print('go')
# n = re.sub(r"\s", ' ', input())
# while len(n) != 0:
#     print(eval_lisp(parse(n), e))
#     n = re.sub(r"\s", ' ', input())
