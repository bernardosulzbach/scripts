#!/usr/bin/env python3
#
# Validates that a whole directory tree is written with slugs.

import argparse
import os
import unicodedata
from slugify import slugify
from hashing import hash_tree


def calculate_moves(root):
    move_list = []
    if not os.path.exists(root):
        print("Provided path does not exist.")
    else:
        for current_directory, directories, files in os.walk(root, topdown=False):
            for file in files:
                filename, file_extension = os.path.splitext(file)
                slug_name = slugify(filename) + file_extension
                if file != slug_name:
                    full_original_path = os.path.join(current_directory, file)
                    full_final_path = os.path.join(current_directory, slug_name)
                    move_list.append((full_original_path, full_final_path))
            for directory in directories:
                slug_directory = slugify(directory)
                if directory != slug_directory:
                    full_original_path = os.path.join(current_directory, directory)
                    full_final_path = os.path.join(current_directory, slug_directory)
                    move_list.append((full_original_path, full_final_path))
    return move_list


def write_required_moves(move_list):
    print("The following moves should be performed:")
    for original, final in move_list:
        print(' ', original, '->', final)


def get_user_friendly_code(root):
    hexadecimal_hash = hash_tree(root)
    # Use only the first four characters hash_tree gives us to make it easier on the user
    pretty_code = hexadecimal_hash[:4]
    return pretty_code


def write_authorization_code(root):
    pretty_code = get_user_friendly_code(root)
    print("Enter the same command followed by '-c {}' to effectively make these changes".format(pretty_code))


def _normalize_caseless(text):
    return unicodedata.normalize("NFKD", text.casefold())


def _equals_ignore_case(a, b):
    """
    Checks if two Unicode strings are equal case-insensitively.
    """
    return _normalize_caseless(a) == _normalize_caseless(b)


def check_authorization_code(root, code):
    valid_code = _equals_ignore_case(get_user_friendly_code(root), code)
    if not valid_code:
        print("The provided authorization code is invalid (should be {})".format(get_user_friendly_code(root)))
    return valid_code


def string_from_move_pair(original, final):
    return "  {} -> {}".format(original, final)


def perform_moves(move_list):
    for original, final in move_list:
        print(string_from_move_pair(original, final))
        os.rename(original, final)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Validates that a whole directory tree is written with slugs.")
    parser.add_argument("root", help="the root of the tree the program will validate")
    parser.add_argument("-c", "--code", help="the authorization code for tree manipulation", required=False)
    arguments = parser.parse_args()
    moves = calculate_moves(arguments.root)
    if len(moves) != 0:
        if not arguments.code:
            write_required_moves(moves)
            write_authorization_code(arguments.root)
        else:
            if check_authorization_code(arguments.root, arguments.code):
                perform_moves(moves)
    else:
        print("Directory tree is valid.")
