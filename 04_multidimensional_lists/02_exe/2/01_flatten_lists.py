line = input().split('|')
sublist = []

for sub_string in line[::-1]:
    sublist.extend(sub_string.split())

print(*sublist)
