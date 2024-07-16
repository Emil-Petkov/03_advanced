import os

file_path = os.path.join('text.txt')

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"File '{file_path}' has been deleted.")

else:
    print("File already deleted!")
