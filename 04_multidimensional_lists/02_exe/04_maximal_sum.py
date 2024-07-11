rows, columns = map(int, input().split())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = float('-inf')
sub_matrix = []

for r in range(rows - 2):
    for c in range(columns - 2):
        firs_row = matrix[r][c:c + 3]
        second_row = matrix[r + 1][c:c + 3]
        third_row = matrix[r + 2][c:c + 3]

        sum_of_sub_matrix = sum(firs_row) + sum(second_row) + sum(third_row)

        if sum_of_sub_matrix > max_sum:
            max_sum = sum_of_sub_matrix
            biggest_matrix = [firs_row, second_row, third_row]

print(f'Sum = {max_sum}')
[print(*row) for row in biggest_matrix]
