even_set = set()
odd_set = set()

for row in range(1, int(input()) + 1):
    ascii_sum_of_name = sum(ord(ch) for ch in input()) // row

    if ascii_sum_of_name % 2 == 0:
        even_set.add(ascii_sum_of_name)

    else:
        odd_set.add(ascii_sum_of_name)

sum_even_set, sum_odd_set = sum(even_set), sum(odd_set)

if sum_even_set == sum_odd_set:
    result = odd_set.union(even_set)

elif sum_odd_set > sum_even_set:
    result = odd_set.difference(even_set)

else:
    result = odd_set.symmetric_difference(even_set)

print(', '.join(map(str, result)))
