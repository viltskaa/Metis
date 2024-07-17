import flask
from flask import Blueprint, jsonify, Response, request

from app.services import ExampleService

example: flask.blueprints.Blueprint = Blueprint('example', __name__)


@example.route('/all', methods=['GET'])
def get_all_examples_from_database() -> Response:
    examples = ExampleService.read_all()

    return jsonify(data=examples)


@example.route('/add', methods=['GET'])
def insert_example_in_database() -> Response:
    name = request.args.get('name', default=None, type=str)
    if name is None:
        return jsonify(data={'error': 'No name provided'})

    success = ExampleService.insert_example(name)
    if not success:
        return jsonify(data={
            'error': 'Failed to insert example',
            'code': ExampleService.LAST_ERROR
        })

    return jsonify(data={'success': success})
