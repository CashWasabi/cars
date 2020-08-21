from typing import Any
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

db_uri = "postgresql://postgres@localhost:5432/postgres"
engine = create_engine(db_uri, convert_unicode=True)

Session = sessionmaker(bind=engine, autocommit=True, autoflush=False)


@contextmanager
def session_context(*args: Any, **kwargs: Any) -> Any:
    session = Session()

    session.begin()

    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise (e)
    finally:
        session.close()
