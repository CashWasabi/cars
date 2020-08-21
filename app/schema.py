from typing import Any

import graphene
from sqlalchemy import and_
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import CarModel


class ActiveSQLAlchemyObjectType(SQLAlchemyObjectType):
    class Meta:
        abstract = True

    @classmethod
    def get_node(cls, info: Any, id: Any) -> Any:
        return cls.get_query(info).filter(
            and_(
                cls._meta.model.deleted_at is None,
                cls._meta.model.id == id
            )
        ).first()


class Car(ActiveSQLAlchemyObjectType):
    class Meta:
        model = CarModel


class Query(graphene.ObjectType):
    Cars = graphene.List(Car)

    def resolve_cars(self, info: Any) -> Any:
        query = Car.get_query(info)  # SQLAlchemy query
        return query.all()


schema = graphene.Schema(query=Query)
