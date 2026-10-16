
import string


def largest_word(sentence):
    words = sentence.split()
    longest = ""

    for word in words:
        clean_word = ""

        for char in word:
            if char not in string.punctuation:
                clean_word += char

        if len(clean_word) > len(longest):
            longest = clean_word

    return longest
