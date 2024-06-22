from collections import deque

children = deque(input().split())
step = int(input())

while not len(children) == 1:
    for i in range(1, step):
        remove_child = children.popleft()
        children.append(remove_child)

    print(f'Removed {children.popleft()}')

print(f'Last is {children.popleft()}')
