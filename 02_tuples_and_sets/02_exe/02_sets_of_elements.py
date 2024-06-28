first_set = set()
second_set = set()

n, m = input().split()

for _ in range(int(n)):
    current_number = int(input())
    first_set.add(current_number)

for _ in range(int(m)):
    current_number = int(input())
    second_set.add(current_number)

print('\n'.join(map(str, first_set.intersection(second_set))))
