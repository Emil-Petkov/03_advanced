row, column = [int(i) for i in input().split(', ')]

sum_of_digits = 0
matrix = []

for row in range(row):
    current_row = list(map(int, input().split(', ')))
    sum_of_digits += sum(current_row)
    matrix.append(current_row)

print(f'{sum_of_digits}\n{matrix}')
