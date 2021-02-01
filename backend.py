import os
import hashlib
import data_base
from functools import partial
from sqlalchemy import create_engine, Column, Integer, String, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def hasher(file_path):

    with open(file_path, mode="rb") as f:
        h = hashlib.md5()
        for buf in iter(partial(f.read, 128), b""):
            h.update(buf)
    return h.hexdigest()


def compute(drirectory, recursevle=True):
    files_data = []
    if recursevle:
        for path, direc, name in os.walk(drirectory):
            if name != []:
                for n in name:
                    file_path = os.path.join(path, n)
                    name, extention = os.path.splitext(n)
                    hashed = hasher(file_path)
                    files_data.append([file_path, name, extention, hashed])

    else:
        for file_name in os.listdir(drirectory):
            if os.path.isfile(os.path.join(drirectory, file_name)):
                file_path = os.path.join(drirectory, file_name)
                name, extention = os.path.splitext(file_name)
                hashed = hasher(file_path)
                files_data.append([file_path, name, extention, hashed])
    return files_data


def delete_duble():

    duble_dict = data_base.get_duble()
    hashes = list(duble_dict.values())
    for o in duble_dict:
        if hashes.count(duble_dict[o]) > 1:
            os.remove(o)
            hashes.remove(duble_dict[o])


if __name__ == "__main__":

    testdir = "/home/tworq/Pulpit/DuplicateCleaner/test_set"

    print(compute(testdir, 0))
