#!/usr/bin/env python3

import os
from slugify import slugify
import sys


def rename(root, old_name, new_name):
    os.rename(os.path.join(root, old_name), os.path.join(root, new_name))
    print("Renamed '{}' to '{}'.".format(old_name, new_name))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Missing arguments.')
    elif len(sys.argv) > 2:
        print('Too many starting points. Pass just the directory you want this script to recurse into.')
    else:
        arg = sys.argv[1]
        if os.path.exists(arg):
            for root, directories, files in os.walk(arg):
                for directory in directories:
                    if directory != slugify(directory):
                        rename(root, directory, slugify(directory))
                for file in files:
                    filename, file_extension = os.path.splitext(file)
                    slug_name = slugify(filename) + file_extension
                    if file != slug_name:
                        rename(root, file, slug_name)
        else:
            print('Given path does not exist.')
