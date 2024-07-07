from collections import deque

chocolates = [int(num) for num in input().split(", ")]
cups_of_milk = deque([int(num) for num in input().split(", ")])

count_milkshakes = 0

while chocolates and cups_of_milk and count_milkshakes < 5:

    value_of_chocolate = chocolates.pop()
    value_of_milk = cups_of_milk.popleft()

    if value_of_chocolate <= 0 and value_of_milk <= 0:
        continue

    if value_of_chocolate <= 0:
        cups_of_milk.appendleft(value_of_milk)
        continue

    if value_of_milk <= 0:
        chocolates.append(value_of_chocolate)
        continue

    elif count_milkshakes == 5:
        break

    if value_of_chocolate == value_of_milk:
        count_milkshakes += 1
    else:
        cups_of_milk.append(value_of_milk)
        chocolates.append(value_of_chocolate - 5)

if count_milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
else:
    print("Milk: empty")
