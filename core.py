def cons(v1, v2):
    return ConsList(v1, v2)


def car(l):
    return l.car()


def cdr(l):
    return l.cdr()


def is_list_empty(l):
    if l.car() is None and l.cdr() is None:
        return True
    return False


def li(v):
    return cons(v, EmptyList())


class ConsList:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def car(self):
        return self.v1

    def cdr(self):
        return self.v2


class EmptyList:
    instance = None

    def __init__(self):
        if not EmptyList.instance:
            EmptyList.instance = ConsList(None, None)

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return 'empty list.'
