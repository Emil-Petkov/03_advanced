n_rows = int(input())

matrix = []
sum_of_diagonal = 0

for _ in range(n_rows):
    matrix.append([int(number) for number in input().split()])

for i in range(n_rows):
    sum_of_diagonal += matrix[i][i]

print(sum_of_diagonal)
