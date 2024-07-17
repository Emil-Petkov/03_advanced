def calculate_sum(number, index=0):
    if index == len(number) - 1:
        return number[index]

    return number[index] + calculate_sum(number, index + 1)


numbers = [int(x) for x in input().split()]
print(calculate_sum(numbers))
