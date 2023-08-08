import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class user(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user = Column(String(250), nullable=False)
    user = relationship( "user", back_populates="favorites")

    
class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    full_name = Column(String(250))
    populations = Column(String(250))
    orbital_period = Column(String(250), nullable=False)
    diameter = Column(String(250))
    climate = Column(String(250))
    favorites = relationship ("Favorites", back_populates =  "planets")

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    full_name = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))
    homeworld = Column(String(250))
    birth_year = Column(String(250), nullable=False)
    characters_id = Column(Integer, ForeignKey('address.id'))
    favorites = relationship ("Favorites", back_populates =  "characters")

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Characters_id = Column(ForeignKey("characters.id"))
    Characters = relationship( "Characters", back_populates="favorites")
    Planets_id = Column(ForeignKey("planets.id"))
    Planets = relationship( "Planets", back_populates="favorites")
    user_id = Column(ForeignKey("user.id"))
    user = relationship( "user", back_populates="favorites")
    



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
