from collections import deque

orders = deque()

total_food = int(input())
food_orders = map(int, input().split())

for order in food_orders:
    orders.append(order)

biggest_order = max(o for o in orders)

while orders:
    next_order = orders.popleft()

    if next_order <= total_food:
        total_food -= next_order

    else:
        orders.appendleft(next_order)
        break

print(f'{biggest_order}')

if orders:
    print(f'Orders left: {" ".join(list(map(str, orders)))}')

else:
    print('Orders complete')
