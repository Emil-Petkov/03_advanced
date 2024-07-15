def factorial(number):
    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


print(factorial(5))

# the better way is to use a for loop
