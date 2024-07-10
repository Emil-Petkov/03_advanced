rows, columns = [int(el) for el in input().split(', ')]

matrix = []

max_sum = float('-inf')

for _ in range(rows):
    matrix.append([int(i) for i in input().split(', ')])

for row_index in range(rows - 1):
    for column_index in range(columns - 1):
        current_element = matrix[row_index][column_index]
        next_element = matrix[row_index][column_index + 1]
        under_element = matrix[row_index + 1][column_index]
        diagonal_element = matrix[row_index + 1][column_index + 1]

        total_sum = current_element + next_element + under_element + diagonal_element

        if total_sum > max_sum:
            max_sum = total_sum
            sub_matrix = [[current_element, next_element], [under_element, diagonal_element]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
