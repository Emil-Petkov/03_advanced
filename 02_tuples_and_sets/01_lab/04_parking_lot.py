parking = set()

for _ in range(int(input())):
    action, registration_number = input().split(', ')

    if action == 'IN':
        parking.add(registration_number)

    elif action == 'OUT':
        parking.remove(registration_number)

if parking:
    print(f'\n'.join(parking))

else:
    print(f'Parking Lot is Empty')
