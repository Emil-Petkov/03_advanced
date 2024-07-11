rows, columns = map(int, input().split())

matrix = [input().split() for _ in range(rows)]

count_sub_matrix = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        symbol = matrix[row][column]

        if (symbol == matrix[row + 1][column] and symbol == matrix[row][column + 1] and
                symbol == matrix[row + 1][column + 1]):
            count_sub_matrix += 1

print(count_sub_matrix)
