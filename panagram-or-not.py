////A pangram is a sentence that contains every single letter of the alphabet at least once. 
////For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
/////Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.


import string


def is_pangram(s):

    letter=string.ascii_lowercase
    # print(letter)
    if letter in s:
        print(True)
    else:
        print(False)


is_pangram('abcdefghijklmnopqrstuvwxyz')
is_pangram('asd')
