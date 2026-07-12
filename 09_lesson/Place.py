from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine("postgresql://postgres:123@localhost:5432/postgres")

class Place(Base):
    __tablename__ = 'places'

    place_id = Column(Integer, primary_key=True)
    place_name = Column(String)
    place_size = Column(Integer)