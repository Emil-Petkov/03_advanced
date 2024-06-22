from collections import deque

initial_water = int(input())
water_in_dispenser = initial_water

queue = deque()

command = input()
while command != "Start":
    queue.append(command)
    command = input()

command = input()

while command != "End":
    if command.startswith("refill"):
        parts = command.split()
        liters_to_add = int(parts[1])
        water_in_dispenser += liters_to_add

    else:
        liters_needed = int(command)
        if queue:
            person = queue.popleft()

            if water_in_dispenser >= liters_needed:
                water_in_dispenser -= liters_needed
                print(f"{person} got water")

            else:
                print(f"{person} must wait")

    command = input()

print(f"{water_in_dispenser} liters left")
