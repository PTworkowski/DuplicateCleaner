import backend
import os


if __name__ == "__main__":

    testdir = "/home/tworq/Pulpit/DuplicateCleaner/test_set"

    for path, dir, name in os.walk(testdir):
        if name != []:
            for n in name:
                print(os.path.join(path, n))
                print(backend.hasher(os.path.join(path, n)))
                print("")
