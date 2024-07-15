def multiply(*args):
    total_sum = 1

    for num in args:
        total_sum *= num

    return total_sum


print(multiply(1, 4, 5))
