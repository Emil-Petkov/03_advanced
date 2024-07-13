def even_odd(*args):
    command = next(com for com in args if isinstance(com, str))

    if command == 'even':
        even_numbers = [num for num in args if isinstance(num, int) and num % 2 == 0]
        return even_numbers

    elif command == 'odd':
        odd_numbers = [num for num in args if isinstance(num, int) and num % 2 != 0]
        return odd_numbers


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
