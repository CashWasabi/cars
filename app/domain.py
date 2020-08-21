from uuid import UUID
from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class Car:
    id: UUID
    license_plate: str
    driver: str
    fuel_capacity: int
    fuel_amount: int
    created: datetime
    modified: datetime
