import os
import hashlib
import data_base
from functools import partial



def hasher(file_path):

    with open(file_path, mode="rb") as f:
        h = hashlib.md5()
        for buf in iter(partial(f.read, 128), b""):
            h.update(buf)
    return h.hexdigest()


def compute(directory, recursive):
    files_data = []
    if recursive:
        for path, direc, name in os.walk(directory):
            if name != []:
                for n in name:
                    file_path = os.path.join(path, n)
                    name, extension = os.path.splitext(n)
                    hashed = hasher(file_path)
                    files_data.append([file_path, name, extension, hashed])

    else:
        for file_name in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, file_name)):
                file_path = os.path.join(directory, file_name)
                name, extension = os.path.splitext(file_name)
                hashed = hasher(file_path)
                files_data.append([file_path, name, extension, hashed])
    return files_data


def delete_duble():

    double_dict = data_base.get_double()
    hashes = list(double_dict.values())
    for o in double_dict:
        if hashes.count(double_dict[o]) > 1:
            os.remove(o)
            hashes.remove(double_dict[o])


if __name__ == "__main__":

    testdir = "/home/tworq/Pulpit/DuplicateCleaner/test_set"

    print(compute(testdir, 0))
