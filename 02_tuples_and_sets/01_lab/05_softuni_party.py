vip_guests = set()
regular_guests = set()

n = int(input())

for _ in range(n):
    reservation_code = input()
    if reservation_code[0].isdigit():
        vip_guests.add(reservation_code)

    else:
        regular_guests.add(reservation_code)

arrived_guests = set()

guest = input().strip()
while guest != "END":
    arrived_guests.add(guest)
    guest = input().strip()

absent_vip = vip_guests - arrived_guests
absent_regular = regular_guests - arrived_guests

print(len(absent_vip) + len(absent_regular))

for guest in sorted(absent_vip):
    print(guest)

for guest in sorted(absent_regular):
    print(guest)
