from sqlmodel import Field, Session, SQLModel, create_engine, or_, select


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=0)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)

        session.commit()


# Code above omitted 👆


def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
    hero_4 = Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32)
    hero_5 = Hero(name="Black Lion", secret_name="Trevor Challa", age=35)
    hero_6 = Hero(name="Dr. Weird", secret_name="Steve Weird", age=36)
    hero_7 = Hero(name="Captain North America", secret_name="Esteban Rogelios", age=93)

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.add(hero_4)
        session.add(hero_5)
        session.add(hero_6)
        session.add(hero_7)

        session.commit()


# Code below omitted 👇


def select_heroes():
    with Session(engine) as session:
        statement = select(Hero)
        results = session.exec(statement)
        for hero in results:
            print(hero)


def select_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.age > 35)
        statement = select(Hero).where(Hero.age >= 35, Hero.age < 40)
        statement = select(Hero).where(Hero.age >= 35).where(Hero.age < 40)
        statement = select(Hero).where(or_(Hero.age <= 35, Hero.age >= 90))

        results = session.exec(statement)
        # print(results)
        # print(results.all())
        print(results.first())


def select_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.age != None)
        results = session.exec(statement)
        hero = results.first()
        print("Hero:", hero)


def select_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Deadpond")
        results = session.exec(statement)
        hero = results.first()
        print("Hero:", hero)


def select_heroes():
    with Session(engine) as session:
        statement = select(Hero).offset(4).limit(2)
        results = session.exec(statement)
        heroes = results.all()
        print(heroes)


def update_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Youngster")
        results = session.exec(statement)
        hero = results.one()
        print("Hero:", hero)
        hero.age = 5098
        session.add(hero)
        session.commit()
        # session.refresh(hero)

        print("Updated hero:", hero.age, hero.name.upper())


# Code above omitted 👆


def update_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        results = session.exec(statement)
        hero_1 = results.one()
        print("Hero 1:", hero_1)

        statement = select(Hero).where(Hero.name == "Captain North America")
        results = session.exec(statement)
        hero_2 = results.one()
        print("Hero 2:", hero_2)

        hero_1.age = 16
        hero_1.name = "Spider-Youngster"
        session.add(hero_1)

        hero_2.name = "Captain North America Except Canada"
        hero_2.age = 110
        session.add(hero_2)

        session.commit()
        session.refresh(hero_1)
        session.refresh(hero_2)

        print("Updated hero 1:", hero_1)
        print("Updated hero 2:", hero_2)


# Code below omitted 👇

# Code above omitted 👆

def delete_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Youngster")
        results = session.exec(statement)
        hero = results.one()
        print("Hero: ", hero)
        session.delete(hero)
        session.commit()
        print("Deleted hero:", hero)
# Code below omitted 👇



def main():
    create_db_and_tables()
    create_heroes()
    # select_heroes()
    # update_heroes()
    # delete_heroes()


if __name__ == "__main__":
    main()
