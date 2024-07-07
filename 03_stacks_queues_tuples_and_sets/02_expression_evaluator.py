from collections import deque

expression = input().split()
copy_expression = expression.copy()

nums = deque()

map_operation = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
}

for el in expression:
    if el in "+-*/":

        while len(nums) > 1:
            left = nums.popleft()
            right = nums.popleft()
            result = map_operation[el](left, right)
            nums.appendleft(result)

    else:
        nums.append(int(el))

print(nums.pop())

# expression = deque(input().split())
# index = 0
#
# while index < len(expression):
#     element = expression[index]
#
#     if element == '*':
#         for _ in range(index - 1):
#             expression.appendleft(int(expression.popleft()) * int(expression.popleft()))
#
#     elif element == '/':
#         for _ in range(index - 1):
#             expression.appendleft(int(expression.popleft()) / int(expression.popleft()))
#     elif element == '+':
#         for _ in range(index - 1):
#             expression.appendleft(int(expression.popleft()) + int(expression.popleft()))
#
#     elif element == '-':
#         for _ in range(index - 1):
#             expression.appendleft(int(expression.popleft()) - int(expression.popleft()))
#
#     if element in '*/+-':
#         del expression[1]
#         index = 1
#
#     index += 1
#
# print(floor(int(expression[0])))
