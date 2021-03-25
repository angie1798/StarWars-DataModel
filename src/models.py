import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water =Column(Integer, nullable=False)
    description=Column(String(250), nullable=False)
    created= Column(String(250), nullable=False)
    edited= Column(String(250), nullable=False)
    url= Column(String(250), nullable=False)
    _id= Column(String(250), nullable=False)

class Persona(Base):
    __tablename__ = 'person'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    height = Column(String(250))
    mass = Column(String(250))
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    description=Column(String(250), nullable=False)
    created= Column(String(250), nullable=False)
    edited= Column(String(250), nullable=False)
    url= Column(String(250), nullable=False)
    _id= Column(String(250), nullable=False)
    homeworld = Column(Integer, ForeignKey('planets.uid'))
    planet = relationship(Planets)

class User(Base):
    __tablename__='user'
    id=Column(Integer, primary_key=True)
    FullName = Column(String(250))
    email = Column(String(250))
    password = Column(String(250))


class Favorites(Base):
    __tablename__='favorites'
    id=Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planets.uid'))
    person_id = Column(Integer, ForeignKey('person.id'))
    planet = relationship(Planets)
    person = relationship(Persona)
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')