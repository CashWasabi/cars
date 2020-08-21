from base import Base
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    TIMESTAMP,
)
from sqlalchemy.dialects.postgresql import UUID


class CarModel(Base):
    __tablename__ = "cars"
    id = Column(UUID(True), primary_key=True)
    license_plate = Column(Unicode, nullable=True)
    driver = Column(Unicode, nullable=True)
    fuel_capacity = Column(Integer, nullable=False)
    fuel_amount = Column(Integer, nullable=False)
    created = Column(TIMESTAMP(True), nullable=False)
    modified = Column(TIMESTAMP(True), nullable=False)
