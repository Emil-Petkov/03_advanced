import os
import re


def read_words(file_path):
    with open(file_path) as file:
        words = [word.lower() for word in file.read().split()]
    return words


def read_content(file_path):
    with open(file_path) as file:
        return file.read().lower()


def count_words(words, content):
    word_count = {}
    for word in words:
        pattern = re.compile(rf'\b{word}\b')
        matches = re.findall(pattern, content)
        word_count[word] = len(matches)
    return word_count


def write_results(output_path, word_count):
    sorted_word_count = sorted(word_count.items(), key=lambda kvp: -kvp[1])
    with open(output_path, 'w') as file:
        for word, count in sorted_word_count:
            file.write(f"{word} - {count}\n")


def main(words_path, text_path, output_path):
    words = read_words(words_path)
    content = read_content(text_path)
    word_count = count_words(words, content)
    write_results(output_path, word_count)
    print(f"Results written to {output_path}")


words_path = os.path.join('words.txt')
text_path = os.path.join('input.txt')
output_path = os.path.join('output.txt')

main(words_path, text_path, output_path)
