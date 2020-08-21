from datetime import datetime
from dataclasses import dataclass, replace

from repositories import CarRepository
from domain import Car
from commands import CreateCar, UpdateCar, ChangeDriver, DeleteCar, RefuelCar


@dataclass
class CreateCarHandler:
    car_repository: CarRepository

    def handle(self, command: CreateCar) -> None:
        car = Car(
            id=command.id,
            license_plate=command.license_plate,
            driver=command.driver,
            fuel_capacity=command.fuel_capacity,
            fuel_amount=command.fuel_amount,
            created=command.created,
            modified=command.modified,
        )
        self.car_repository.add(car)


@dataclass
class UpdateCarHandler:
    car_repository: CarRepository

    def handle(self, command: UpdateCar) -> None:
        car = self.car_repository.get_by_id(command.id)
        updated_car = replace(
            car,
            license_plate=command.license_plate,
            driver=command.driver,
            fuel_capacity=command.fuel_capacity,
            fuel_amount=command.fuel_amount,
            modified=datetime.now().isoformat(),
        )
        self.car_repository.update(updated_car)


@dataclass
class ChangeDriverHandler:
    car_repository: CarRepository

    def handle(self, command: ChangeDriver) -> None:
        car = self.car_repository.get_by_id(command.id)
        updated_car = replace(
            car, driver=command.driver, modified=datetime.now().isoformat()
        )
        self.car_repository.update(updated_car)


@dataclass
class RefuelCarHandler:
    car_repository: CarRepository

    def handle(self, command: RefuelCar) -> None:
        car = self.car_repository.get_by_id(command.id)
        updated_car = replace(
            car, fuel_amount=car.fuel_capacity, modified=datetime.now().isoformat()
        )
        self.car_repository.update(updated_car)


@dataclass
class DeleteCarHandler:
    car_repository: CarRepository

    def handle(self, command: DeleteCar) -> None:
        self.car_repository.delete(command.id)
