mathematical_expression = input()

open_bracket_stack = []

for index in range(len(mathematical_expression)):
    char = mathematical_expression[index]

    if char == '(':
        open_bracket_stack.append(index)

    if char == ')':
        if open_bracket_stack:
            open_bracket_index = open_bracket_stack.pop()
            close_bracket_index = index

            print(mathematical_expression[open_bracket_index:close_bracket_index + 1])
