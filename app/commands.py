from datetime import datetime
from uuid import UUID
from dataclasses import dataclass


@dataclass(frozen=True)
class CreateCar:
    id: UUID
    license_plate: str
    driver: str
    fuel_capacity: int
    fuel_amount: int
    created: datetime
    modified: datetime


@dataclass(frozen=True)
class UpdateCar:
    license_plate: str
    driver: str
    fuel_capacity: int
    fuel_amount: int
    modified: datetime


@dataclass(frozen=True)
class ChangeDriver:
    id: UUID
    driver: str


@dataclass(frozen=True)
class RefuelCar:
    id: UUID


@dataclass(frozen=True)
class DeleteCar:
    id: UUID
