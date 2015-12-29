#!/usr/bin/env python3

import argparse
import collections
import string


def make_punctuation_translation_table():
    # It is safer to replace punctuation by spaces as it prevents merging incorrectly separated words together.
    return str.maketrans(string.punctuation, ' ' * len(string.punctuation))


def count_words(text):
    text = text.lower().translate(make_punctuation_translation_table())
    dictionary = collections.defaultdict(lambda: 0)
    for gram in text.split():
        dictionary[gram] += 1
    return dictionary


def norm(vector):
    return sum(x ** 2 for x in vector) ** .5


def write_dictionary(dictionary):
    lines = []
    for key, value in sorted(dictionary.items(), key=lambda entry: entry[1], reverse=True):  # Sort by value
        lines.append(" '{}': {}".format(key, value))
    print('\n'.join(lines))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Uses cosine similarity to estimate document distance.")
    parser.add_argument("a", help="a text file")
    parser.add_argument("b", help="a text file")
    parser.add_argument("-v", "--verbose", action="store_true", help="display word counts")
    arguments = parser.parse_args()
    with open(arguments.a, 'r') as a_file:
        with open(arguments.b, 'r') as b_file:
            a_words = count_words(' '.join(a_file.readlines()))
            b_words = count_words(' '.join(b_file.readlines()))
            if arguments.verbose:
                print("Word count of", arguments.a)
                write_dictionary(a_words)
                print("Word count of", arguments.b)
                write_dictionary(b_words)
            numerator = 0
            for word in a_words.keys():
                numerator += a_words[word] * b_words[word]
            result = 0
            if numerator != 0:
                denominator = norm(a_words.values()) * norm(b_words.values())
                result = numerator / denominator
            print("cos(θ)", "=", result)
