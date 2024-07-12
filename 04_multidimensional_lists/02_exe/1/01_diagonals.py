rows = int(input())

matrix = [[int(el) for el in input().split(', ')] for _ in range(rows)]

primary_diagonal = [matrix[r][r] for r in range(rows)]
secondary_diagonal = [matrix[r][rows - r - 1] for r in range(rows)]

print(f'Primary diagonal: {", ".join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}')
