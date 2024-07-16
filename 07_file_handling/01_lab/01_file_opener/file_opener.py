import os

path_to_file = os.path.join('text.txt')

try:
    open_file = open(path_to_file)
    print('File Found : )')

except FileNotFoundError:
    print('File Not Found')
