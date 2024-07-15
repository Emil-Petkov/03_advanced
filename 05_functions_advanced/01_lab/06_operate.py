from functools import reduce


def operate(opr, *args):
    if opr == '+':
        return reduce(lambda x, y: x + y, args)

    elif opr == '-':
        return reduce(lambda x, y: x - y, args)

    elif opr == '*':
        return reduce(lambda x, y: x * y, args)

    elif opr == '/':
        return reduce(lambda x, y: x / y, args)


print(operate("+", 1, 2, 3))
print(operate("-", 1, 2, 3))
print(operate("*", 1, 2, 3))
print(operate("/", 1, 2, 3))
