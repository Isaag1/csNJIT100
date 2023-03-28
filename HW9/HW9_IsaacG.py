"""
Isaac Guerrero
CS 100 Section 015
HW09,November 9, 2021
"""
# 1
import string


def file_copy(in_file, out_file):
    with open(in_file, 'r') as f_in:
        with open(out_file, 'w') as f_out:
            f_out.write(f_in.read())
    print(f"Contents of {in_file} copied to {out_file}.")
    


# 2
def file_stats(in_file):
    with open(in_file, 'r') as f:
        content = f.read()
        num_lines = len(content.split('\n'))
        num_words = len(content.split())
        num_chars = len(content)
    print(f"lines {num_lines}\nwords {num_words}\ncharacters {num_chars}")


# 3


def repeat_words(in_file, out_file):
    with open(in_file, 'r') as f_in:
        with open(out_file, 'w') as f_out:
            for line in f_in:
                words = line.lower().translate(str.maketrans('', '', string.punctuation)).split()
                repeat_words = set()
                for word in set(words):
                    if words.count(word) > 1:
                        repeat_words.add(word)
                f_out.write(' '.join(repeat_words) + '\n')
    print(f"Repeated words written to {out_file}.")
file_copy("input.txt", "output.txt")
file_stats("input.txt")
repeat_words("input.txt", "repeat.txt")
