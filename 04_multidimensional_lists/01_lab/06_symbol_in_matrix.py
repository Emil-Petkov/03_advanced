

matrix = []

for _ in range(int(input())):
    matrix.append(list(input()))

search_symbol = input()

for row_index, row in enumerate(matrix):
    for column_index, element in enumerate(row):
        if search_symbol == element:
            print(f'({row_index}, {column_index})')
            exit()

print(f'{search_symbol} does not occur in the matrix')
