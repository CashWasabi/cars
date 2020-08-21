import json
from datetime import datetime
from uuid import UUID, uuid4

from flask import Blueprint, Response, request, make_response, jsonify

from commands import CreateCar, DeleteCar, UpdateCar, ChangeDriver, RefuelCar
from repositories import CarRepository
from handlers import (
    CreateCarHandler,
    DeleteCarHandler,
    UpdateCarHandler,
    ChangeDriverHandler,
    RefuelCarHandler,
)
from queries import CarQuery

api = Blueprint("car", __name__)


@api.route("/car/<car_id>", methods=["GET"])
def get_car(car_id: UUID) -> Response:
    car = CarRepository.get_by_id(car_id)
    return jsonify(car)


@api.route("/car", methods=["GET"])
def get_cars() -> Response:
    limit = request.args.get("limit", 0, int)
    offset = request.args.get("offset", 0, int)
    cars, total = CarQuery.find_cars(limit, offset)
    return jsonify({})


@api.route("/car/search", methods=["POST"])
def search_car() -> Response:
    data = request.get_json()
    result = CarQuery.search_car(data["query"])
    return jsonify(result.data)


@api.route("/car", methods=["POST"])
def create_car(car_id: UUID) -> Response:
    data = request.get_json()
    command = CreateCar(
        id=uuid4(),
        license_plate=data.get("licensePlate", ""),
        driver=data.get("driver", ""),
        fuel_capacity=data.get("fuelCapacity", 0),
        fuel_ammount=data.get("fuelAmount", 0),
        created=datetime.now(),
        modified=None
    )
    handler = CreateCarHandler(command)
    handler.handle(command)
    return make_response("", 204)


@api.route("/car/<car_id>", methods=["DELETE"])
def delete_car(car_id: UUID) -> Response:
    command = DeleteCar()
    handler = DeleteCarHandler(command)
    handler.handle(command)
    return make_response("", 204)


@api.route("/car/<car_id>", methods=["PUT"])
def update_car(car_id: UUID) -> Response:
    data = request.get_json()
    command = UpdateCar(
        license_plate=data.get("licensePlate", ""),
        driver=data.get("driver", ""),
        fuel_capacity=data.get("fuelCapacity", 0),
        fuel_ammount=data.get("fuelAmount", 0),
        modified=datetime.now()
    )
    handler = UpdateCarHandler(command)
    handler.handle(command)
    return make_response("", 204)


@api.route("/car/<car_id>/change-driver", methods=["PUT"])
def change_driver(car_id: UUID) -> Response:
    data = request.get_json()
    command = ChangeDriver(
        id=car_id,
        driver=data["driver"]
    )
    handler = ChangeDriverHandler(command)
    handler.handle(command)
    return make_response("", 204)


@api.route("/car/<car_id>/refuel-car", methods=["POST"])
def refuel_car(car_id: UUID) -> Response:
    command = RefuelCar(car_id)
    handler = RefuelCarHandler(command)
    handler.handle(command)
    return make_response("", 204)
