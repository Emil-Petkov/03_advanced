














n_lines = int(input())
numbers = []

for _ in range(n_lines):
    operation = input().split()

    if operation[0] == '1':
        add_number = int(operation[1])
        numbers.append(add_number)

    elif operation[0] == '2' and numbers:
        numbers.pop()

    elif operation[0] == '3' and numbers:
        print(max(numbers))

    elif operation[0] == '4' and numbers:
        print(min(numbers))

result = (', '.join(map(str, reversed(numbers))))

print(result)
