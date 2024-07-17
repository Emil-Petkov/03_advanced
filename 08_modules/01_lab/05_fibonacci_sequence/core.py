def create_sequence(number):
    list_of_sequence = [0, 1]

    for _ in range(number - 2):
        next_number = list_of_sequence[-1] + list_of_sequence[-2]
        list_of_sequence.append(next_number)

    return list_of_sequence


def locate_number(number, sequence):
    try:
        return sequence.index(number)

    except ValueError:
        return f'The number {number} is not in the sequence'
