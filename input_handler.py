def check_brackets(string):
    stack = []
    for i in string:
        if i is '(':
            stack.append(i)

        if i is ')':
            if len(stack) == 0:
                return False

            stack.pop()

    if len(stack) == 0:
        return True

    return False


def pinch_block(string):
    if not check_brackets(string):
        return Exception('Incorrect brackets!')

    stack = []
    result = 0

    for i in string:
        result += 1

        if i is '(':
            stack.append(i)

        if i is ')':
            if len(stack) == 0:
                raise Exception('Wrong input!')

            stack.pop()
            if len(stack) == 0:
                return result

    raise Exception('Wrong input!')
