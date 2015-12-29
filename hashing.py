import os
import hashlib


def _update_sha256(filename, sha256):
    """
    Updates a SHA-256 algorithm with the filename and the contents of a file.
    """
    block_size = 64 * 1024  # 64 KB
    with open(filename, 'rb') as input_file:
        while True:
            data = input_file.read(block_size)
            if not data:
                break
            sha256.update(data)
    sha256.update(filename.encode("utf-8"))
    return sha256


def hash_tree(root):
    """
    Returns a cryptographically secure hash for a whole directory tree taking into account the names and the content of
    the files.
    """
    file_list = []
    for root_directory, directories, files in os.walk(root):
        for file in files:
            file_list.append(os.path.join(root_directory, file))
    sorted_file_list = sorted(file_list)
    sha256 = hashlib.sha256()
    for file in sorted_file_list:
        _update_sha256(file, sha256)
    return sha256.hexdigest()
