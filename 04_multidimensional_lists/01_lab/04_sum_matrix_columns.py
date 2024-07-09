rows, cols = map(int, input().split(', '))

matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

col_sums = [sum(matrix[row][col] for row in range(rows)) for col in range(cols)]

print(*col_sums, sep='\n')
