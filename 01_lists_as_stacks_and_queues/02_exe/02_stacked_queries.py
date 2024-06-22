n_lines = int(input())
numbers = []

for _ in range(n_lines):
    operation = input().split()

    if operation[0] == '2':
        if numbers:
            numbers.pop()

    elif operation[0] == '3':
        if numbers:
            print(max(numbers))

    elif operation[0] == '4':
        if numbers:
            print(min(numbers))

    else:
        add_number = int(operation[1])
        numbers.append(add_number)

result = (', '.join(map(str, reversed(numbers))))

print(result)
