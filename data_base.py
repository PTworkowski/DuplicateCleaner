
import os

from sqlalchemy import create_engine, Column, Integer, String, insert, distinct
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///:memory:", echo=False)

Base = declarative_base()
Session = sessionmaker(bind=engine)


class DoubleFiles(Base):
    __tablename__ = "files"

    file_id = Column(Integer, primary_key=True, autoincrement=True)
    file_path = Column(String(250), nullable=False)
    file_name = Column(String(250), nullable=False)
    file_ext = Column(String(5), nullable=False)
    file_hash = Column(String(32), nullable=False)

    def __repr__(self):
        return f"File: {self.file_name} - hash MD5: {self.file_hash}"


def build_db():
    if os.path.exists("file_data.sqlite"):
        os.remove("file_data.sqlite")
    Base.metadata.create_all(engine)


def put_in_db(file_data):

    session1 = Session()

    for obj in file_data:
        rec = DoubleFiles(
            file_path=obj[0], file_name=obj[1], file_ext=obj[2], file_hash=obj[3]
        )
        session1.add(rec)

    session1.commit()


def show_all():

    session2 = Session()
    i = 1
    for f in session2.query(DoubleFiles).order_by(DoubleFiles.file_name):

        print("{:5.0f} {:50s}{:50s}".format(i, f.file_name, f.file_hash))
        i += 1
    session2.commit()


def show_double():
    session3 = Session()
    i = 1
    resolute = {}
    for d in session3.query(DoubleFiles).order_by(DoubleFiles.file_hash):
        if (
            session3.query(DoubleFiles)
            .filter(DoubleFiles.file_hash == d.file_hash)
            .count()
            > 1
        ):
            print("{:3.0f} {:50s}{:50s}".format(i, d.file_name, d.file_hash))
            resolute[d.file_path] = d.file_hash
            i += 1
    session3.commit()
    return resolute


def get_double():
    session4 = Session()
    i = 1
    resolute = {}
    for d in session4.query(DoubleFiles).order_by(DoubleFiles.file_hash):
        if (
            session4.query(DoubleFiles)
            .filter(DoubleFiles.file_hash == d.file_hash)
            .count()
            > 1
        ):
            resolute[d.file_path] = d.file_hash
            i += 1
    session4.commit()
    return resolute

