from flask import Flask
from flask_graphql import GraphQLView

from api import api as car_api
from database import init_db
from schema import schema


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(car_api)
    return app


init_db()
app = create_app()

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # for having the GraphiQL interface
    )
)

app.run(debug=True)
