text = input()
try:
    n = int(input())

    print(text * n)

except ValueError:
    print('Variable times must be an integer.')
