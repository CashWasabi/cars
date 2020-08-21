from base import Base, engine
from models import CarModel


print("Creating database and tables ...")
CarModel = CarModel


def init_db():
    # Create All Tables
    Base.metadata.create_all(engine)


print("Creation done.")
