import flask

from .V1 import example

ROUTES: list[flask.blueprints.Blueprint] = [
    example,
]
