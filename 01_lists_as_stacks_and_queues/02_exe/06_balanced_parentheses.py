from collections import deque


def is_balanced(sequence):
    stack = deque()
    matching_parentheses = {')': '(', ']': '[', '}': '{'}

    for char in sequence:
        if char in matching_parentheses.values():
            stack.append(char)

        elif char in matching_parentheses.keys():
            if stack and stack[-1] == matching_parentheses[char]:
                stack.pop()

            else:
                return "NO"

    return "YES" if not stack else "NO"


data_input = input()
print(is_balanced(data_input))
