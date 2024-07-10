











rows = int(input())

matrix = []
for _ in range(rows):
    matrix.append([[int(el)] for el in input().split(', ')])

primary_diagonal = []
secondary_diagonal = []

for i in range(rows):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][rows - i - 1])

result_primary_diagonal = [item for sublist in primary_diagonal for item in sublist]
result_secondary_diagonal = [item for sublist in secondary_diagonal for item in sublist]

print(f'Primary diagonal: {", ".join(map(str, result_primary_diagonal))}. Sum: {sum(result_primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(map(str, result_secondary_diagonal))}. Sum: {sum(result_secondary_diagonal)}')
