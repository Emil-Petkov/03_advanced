def check_numbers(numbers):
    positive_numbers_result = sum(x for x in numbers if x > 0)
    negative_numbers_result = sum(x for x in numbers if x < 0)

    print(f'{negative_numbers_result}\n{positive_numbers_result}')

    if abs(positive_numbers_result) < abs(negative_numbers_result):
        print('The negatives are stronger than the positives')
    else:
        print(f'The positives are stronger than the negatives')


numbers = [int(x) for x in input().split()]

check_numbers(numbers)
