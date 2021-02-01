import backend
from functools import partial
from sqlalchemy import create_engine, Column, Integer, String, insert, distinct
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///:memory:", echo=False)

Base = declarative_base()
Sesion = sessionmaker(bind=engine)


class DubbleFiles(Base):
    __tablename__ = "files"

    file_id = Column(Integer, primary_key=True, autoincrement=True)
    file_path = Column(String(250), nullable=False)
    file_name = Column(String(250), nullable=False)
    file_ext = Column(String(5), nullable=False)
    file_hash = Column(String(32), nullable=False)

    def __repr__(self):
        return f"File: {self.file_name} - hash MD5: {self.file_hash}"


def bild_db():

    Base.metadata.create_all(engine)


def put_in_db(file_data):

    sesion1 = Sesion()

    for obj in file_data:
        rec = DubbleFiles(
            file_path=obj[0], file_name=obj[1], file_ext=obj[2], file_hash=obj[3]
        )
        sesion1.add(rec)

    sesion1.commit()


def show_all():

    sesion2 = Sesion()
    i = 1
    for f in sesion2.query(DubbleFiles):

        print("{:5.0f} {:50s}{:50s}".format(i, f.file_name, f.file_hash))
        i += 1
    sesion2.commit()


def show_duble():
    sesion3 = Sesion()
    i = 1
    resolut = {}
    for d in sesion3.query(DubbleFiles).order_by(DubbleFiles.file_hash):
        if (
            sesion3.query(DubbleFiles)
            .filter(DubbleFiles.file_hash == d.file_hash)
            .count()
            > 1
        ):
            print("{:3.0f} {:50s}{:50s}".format(i, d.file_name, d.file_hash))
            resolut[d.file_path] = d.file_hash
            i += 1
    sesion3.commit()
    return resolut


def get_duble():
    sesion4 = Sesion()
    i = 1
    resolut = {}
    for d in sesion4.query(DubbleFiles).order_by(DubbleFiles.file_hash):
        if (
            sesion4.query(DubbleFiles)
            .filter(DubbleFiles.file_hash == d.file_hash)
            .count()
            > 1
        ):
            resolut[d.file_path] = d.file_hash
            i += 1
    sesion4.commit()
    return resolut
