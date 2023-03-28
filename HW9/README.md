# Problem 1
Write a function file_copy that takes two string parameters (in_file andout_file) and copies the content of in_file intoout_file. Assume that in_file exists before file_copy is called. For example, the following would be correct input and output:
>>> file_copy('created_equal.txt', 'copy.txt')
>>> copy_f = open('copy.txt')
>>> copy_f.read()
We hold these truths to be self-evident,\nthat all men are created equal\n'
# Problem 2
Write a function named file_stats that takes one string parameter (in_file) that is the name of an existing text file. The function file_stats should calculate three statistics a boutin_file: the number of lines it contains, the number of words and the number of characters, and print the three statistics on separate lines. For example, the following would be correct input and output:
>>> file_stats('created_equal.txt')
- lines 2
- words 13
- characters 72
# Problem 3
Write a function named repeat_words that takes two string parameters:
- 1. in_file: the name of an input file that exists before repeat_words is called
- 2. out_file: the name of an output file that repeat_words creates
Assume that the input file is in the current working directory and write the output file to that directory.
For each line of the input file, the function repeat_words should write to the output file all of the words that appear more than once on that line. Each word should be lower cased and stripped of leading and trailing punctuation. Each repeated word on a line should be written to the corresponding line of the output file only once, regardless of the number of times the word is repeated.
