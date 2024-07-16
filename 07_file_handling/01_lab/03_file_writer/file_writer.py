import os

file_path = os.path.join('text.txt')

with open(file_path, 'w') as file:
    file.write('I just created my first file!')
