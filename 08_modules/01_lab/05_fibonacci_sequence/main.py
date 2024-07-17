from core import create_sequence, locate_number

command = input()
sequence = []

while command != 'Stop':
    if command.startswith('Create'):
        _, _, number = command.split()
        number = int(number)
        sequence = create_sequence(number)
        print(*sequence)

    elif command.startswith('Locate'):
        _, number = command.split()
        number = int(number)
        result = locate_number(number, sequence)
        print(result)

    command = input()
