"""
Isaac Guerrero
CS 100 Section 015
HW09,November 9, 2021
"""
#1
def file_copy(in_file, out_file):
    with open(in_file, 'r') as f1:
        with open(out_file, 'w') as f2:
            for line in f1:
                f2.write(line)

   
#2
def file_stats(in_file):
    with open(in_file, 'r') as f:
        lines = 0
        words = 0
        chars = 0
        for line in f:
            lines += 1
            words += len(line.split())
            chars += len(line)
        print(f'lines {lines}')
        print(f'words {words}')
        print(f'characters {chars}')


#3
import string

def repeat_words(in_file, out_file):
    with open(in_file, 'r') as f1:
        with open(out_file, 'w') as f2:
            for line in f1:
                words = line.strip().lower().translate(str.maketrans('', '', string.punctuation)).split()
                repeated_words = set()
                for word in set(words):
                    if words.count(word) > 1:
                        repeated_words.add(word)
                f2.write(' '.join(repeated_words) + '\n')
