rows = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

primary_diagonal = [matrix[r][r] for r in range(rows)]
secondary_diagonal = [matrix[r][rows - r - 1] for r in range(rows)]

diagonal_difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))

print(diagonal_difference)
