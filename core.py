def cons(v1, v2):
    return ConsList(v1, v2)


def car(l):
    return l.car()


def cdr(l):
    return l.cdr()


def is_empty(l):
    if l.car() is None and l.cdr() is None:
        return True
    return False


def get_type(o):
    try:
        return o.get_type()
    except:
        return type(o)


def get_value(o):
    try:
        return o.get_value()
    except:
        return o


class ConsList:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.type = 'ConsList'

    def car(self):
        return self.v1

    def cdr(self):
        return self.v2

    def get_type(self):
        return self.type


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


class Symbol:
    def __init__(self, v):
        self.val = v
        self.type = 'Symbol'

    def get_value(self):
        return self.val


class BinOp:
    def __init__(self, op):
        self.op = op
        self.type = 'BinOp'

    def get_type(self):
        return self.type

    def get_value(self):
        return self.op
