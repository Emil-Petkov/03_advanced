import os

path = os.path.join('text.txt')

with open(path, 'r') as file:
    content = file.read()
    print(content)
