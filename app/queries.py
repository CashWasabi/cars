from typing import Any

from uuid import UUID

from typing import Optional, Tuple

from sqlalchemy import func

from base import session_context
from models import CarModel
from schema import schema
from domain import Car


class CarQuery:
    @staticmethod
    def find_car(car_id: UUID) -> Optional[Car]:
        return None

    @staticmethod
    def find_cars(limit: int = 100, offset: int = 0) -> Tuple[Car, int]:
        with session_context() as session:
            result = (
                session.query(
                    CarModel,
                    func.count(CarModel.id).over().label("total")
                )
                .limit(limit)
                .offset(offset)
                .all()
            )

            total = 0
            cars = []
            for car, total in result:
                cars.append(
                    Car(
                        id=car.id,
                        license_plate=car.license_plate,
                        driver=car.driver,
                        fuel_capacity=car.fuel_capacity,
                        fuel_amount=car.fuel_amount,
                        created=car.created,
                        modified=car.modified,
                    )
                )

            return cars, total

    @staticmethod
    def search_car(query: str) -> Any:
        with session_context() as session:
            result = schema.execute(
                query,
                context_value={'session': session}
            )
        return result
