"""
I will learn how to use sqlite3 database system
mainly using the SQLMODEL
Library mainly
Here i can just make "uv sync"
And then i can start using sqlmodel easily
for now here is no code

"""

from typing import Optional

from sqlmodel import Field, SQLModel
from sqlmodel import create_engine
from sqlmodel import Session


class Hero(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()
