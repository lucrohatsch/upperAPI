from sqlalchemy import Column, Integer, String, Float, ForeignKey
import sqlalchemy.orm as _orm
import db_conect as _db


class User (_db.base):
    __tablename__= "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    pss = Column(String)


class Registers(_db.base):
    __tablename__="registers"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    field_1 = Column(String)
    author=Column(String)
    description=Column(String)
    my_numeric_field=Column(Integer)


