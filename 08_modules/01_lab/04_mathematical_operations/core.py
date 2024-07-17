def add(number_one, number_two):
    return number_one + number_two


def subtract(number_one, number_two):
    return number_one - number_two


def multiply(number_one, number_two):
    return number_one * number_two


def divide(number_one, number_two):
    return number_one / number_two


def power(number_one, number_two):
    return number_one ** number_two


mapper = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '^': power,
}


def execute_expression(expression):
    number_one, operator, number_two = expression.split()

    number_one = float(number_one)
    number_two = float(number_two)

    return mapper[operator](number_one, number_two)
