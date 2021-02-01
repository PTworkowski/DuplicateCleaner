import data_base
import backend
import os

testdir = "/home/tworq/Pulpit/DuplicateCleaner/test_set"
if os.path.exists("filedata.sqlite"):
    os.remove("filedata.sqlite")

data_base.bild_db()

files_data = backend.compute(testdir, 1)

data_base.put_in_db(files_data)

data_base.show_all()

duble_dict = data_base.show_duble()

backend.delete_duble()
