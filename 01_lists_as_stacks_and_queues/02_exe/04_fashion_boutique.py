











from collections import deque

clothes_in_the_box = deque(map(int, input().split()))
capacity_of_one_rack = int(input())

sum_of_added_clothes = 0

n_racks = 1

while clothes_in_the_box:
    next_clothes = clothes_in_the_box.popleft()

    if sum_of_added_clothes + next_clothes > capacity_of_one_rack:
        n_racks += 1
        sum_of_added_clothes = next_clothes

    else:
        sum_of_added_clothes += next_clothes

print(n_racks)
