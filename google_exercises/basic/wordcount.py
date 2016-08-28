#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

def print_words(filename):
    word_occurrences = builder_word_count_helper(filename)
    for element in sorted(word_occurrences):
        print('Word: ' + element + ' - Number of ocurrences: ' + str(word_occurrences[element]))
    
def print_top(filename):
    title_description = '\nTop {0} occurrences from file ' + filename + '\n'
    word_occurrences = builder_word_count_helper(filename)
    top_occurrences = sorted(tuple(word_occurrences.items())
                                ,key=lambda tuple : tuple[-1]
                                    , reverse=True)

    if len(top_occurrences) >= 20:
        print(title_description.format(20))
        for top_element in range(20):
            print("Word: {0} - Number of Ocurrences: {1}".format(top_occurrences[top_element][0],
                                                             top_occurrences[top_element][-1]))
            print(top_occurrences[top_element])
    else:
        print(title_description.format(len(top_occurrences)))
        for element in top_occurrences:
            print("Word: {0} - Number of Ocurrences: {1}".format(element[0], element[-1]))


def builder_word_count_helper(filename):
    word_count_dictionary = {}
    words = get_words_from_file(filename)
    for word in words:
        number_of_ocurrences = 0        
        if word not in word_count_dictionary:
            word_count_dictionary[word] = number_of_ocurrences
        for compare_word in words:
            if word == compare_word:
                number_of_ocurrences += 1
                word_count_dictionary[word] = number_of_ocurrences
    return word_count_dictionary


def get_words_from_file(filename):
    return str(get_file_content(filename)).lower().split()


def get_file_content(filename):
    file = open(filename)
    file_content = file.read()
    file.close()


    file_content = file_content.replace('\n', '')

    #for denied_character in "?.;":
       # file_content = file_content.replace(denied_character, '  ')

    return str(file_content)

# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print ('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print ('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
