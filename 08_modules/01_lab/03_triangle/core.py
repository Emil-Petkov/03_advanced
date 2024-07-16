def print_triangle(n):
    first_part_of_triangle(n)
    second_part_of_triangle(n)


def first_part_of_triangle(n):
    for row in range(1, n + 1):
        for num in range(1, row + 1):
            print(num, end=' ')

        print()


def second_part_of_triangle(n):
    for row in range(n, 0, -1):
        for num in range(1, row):
            print(num, end=' ')

        print()



