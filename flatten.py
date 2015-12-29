#!/usr/bin/env python3
#
# Moves all files in all directories to the root directory, renaming them using MD5 hashes.
#
# If I am not mistaken, this script requires at least Python 3.4 because it relies on __file__ being absolute.


import hashlib
import os
import shutil


def md5(filename):
    """
    Creates the MD5 hash of a file.
    :param filename: the name of the file, a string
    """
    # Ensure that this script is not going to grab huge amounts of memory at once.
    block_size = 65536  # 64 KB.
    hash_function = hashlib.md5()
    with open(filename, 'rb') as f:
        buf = f.read(block_size)
        while len(buf) > 0:
            hash_function.update(buf)
            buf = f.read(block_size)
    return hash_function.hexdigest()


if __name__ == '__main__':
    for root, directories, files in os.walk('.'):
        for file in files:
            complete_name = os.path.join(root, file)
            if complete_name != __file__:
                # Preserve the file extension
                extension = os.path.splitext(file)[1]
                hex_hash = md5(complete_name)
                # TODO: check for hash collisions
                shutil.move(complete_name, hex_hash + extension)
