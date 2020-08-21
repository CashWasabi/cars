from flask import Flask

from api import api as car_api
from database import init_db


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(car_api)
    return app


init_db()
app = create_app()
app.run(debug=True)
