from uuid import UUID
from base import session_context
from models import CarModel
from domain import Car


class CarRepository:
    @staticmethod
    def add(car: Car) -> None:
        with session_context() as session:
            model = CarModel(
                id=car.id,
                license_plate=car.license_plate,
                driver=car.driver,
                fuel_capacity=car.fuel_capacity,
                fuel_amount=car.fuel_amount,
                created=car.created,
                modified=car.modified,
            )
            session.add(model)

    @staticmethod
    def update(car: Car) -> None:
        with session_context() as session:
            model = CarModel(
                id=car.id,
                license_plate=car.license_plate,
                driver=car.driver,
                fuel_capacity=car.fuel_capacity,
                fuel_amount=car.fuel_amount,
                created=car.created,
                modified=car.modified,
            )
            session.update(model)

    @staticmethod
    def delete(car_id: UUID) -> None:
        with session_context() as session:
            session.query(CarModel).filter_by(id=car_id).delete()

    @staticmethod
    def get_by_id(car_id: UUID) -> Car:
        with session_context() as session:
            model = session.query(CarModel).filter_by(id=car_id).one()
            car = Car(
                id=model.id,
                license_plate=model.license_plate,
                driver=model.driver,
                fuel_capacity=model.fuel_capacity,
                fuel_amount=model.fuel_amount,
                created=model.created,
                modified=model.modified,
            )
            return car
