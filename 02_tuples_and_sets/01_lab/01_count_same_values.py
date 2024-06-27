data = tuple([float(num) for num in input().split()])

count_values = {}

for number in data:
    if number not in count_values:
        count_values[number] = data.count(number)

for k, v in count_values.items():
    print(f'{k} - {v} times')
