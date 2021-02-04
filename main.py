import data_base
import backend
import argparse


parser = argparse.ArgumentParser()
### options for parser
parser.add_argument("path", help="path to directory You want to scan", type=str)
parser.add_argument("-a", "--all", help="if given will scan subfolders", action="store_true")
parser.add_argument("-d", "--duble", help="if given will scan subfolders", action="store_true")

args = parser.parse_args()

# testdir = "/home/tworq/PycharmProjects/DuplicateCleaner/test_set"
### building DB with files in directory
data_base.build_db()
if args.all:
    files_data = backend.compute(args.path, recursive=True)
else:
    files_data = backend.compute(args.path, recursive=False)
data_base.put_in_db(files_data)

data_base.show_all()
#double_dict = data_base.show_duble()
# backend.delete_double()
