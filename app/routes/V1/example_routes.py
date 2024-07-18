import flask
from flask import Blueprint, Response, request, current_app, json

from app.services import ExampleService

example: flask.blueprints.Blueprint = Blueprint('example', __name__)


@example.route('/all', methods=['GET'])
def get_all_examples_from_database() -> Response:
    examples = ExampleService.read_all()

    return current_app.response_class(
        response=json.dumps(examples),
        status=200,
        mimetype='application/json'
    )


@example.route('/add', methods=['GET'])
def insert_example_in_database() -> Response:
    name = request.args.get('name', default=None, type=str)

    if name is None:
        return current_app.response_class(
            response=json.dumps({'error': 'No name provided'}),
            status=400,
            mimetype='application/json'
        )

    success = ExampleService.insert_example(name)
    if success:
        return current_app.response_class(
            response=json.dumps({'error': 'No name provided'}),
            status=200,
            mimetype='application/json'
        )

    return current_app.response_class(
        response=json.dumps({'error': 'Name already exists'}),
        status=409,
        mimetype='application/json'
    )
