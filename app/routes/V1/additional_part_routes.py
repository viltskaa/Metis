import flask
from flask import Blueprint, Response, request, current_app, json

from app.services import AdditionalPartService

add_part: flask.blueprints.Blueprint = Blueprint('add_part', __name__)


@add_part.route('/all', methods=['GET'])
def get_all_add_parts_from_database() -> Response:
    add_parts = AdditionalPartService.read_all()

    return current_app.response_class(
        response=json.dumps(add_parts),
        status=200,
        mimetype='application/json'
    )


@add_part.route('/get', methods=['GET'])
def get_add_part_by_id() -> Response:
    part_id = request.args.get('part_id', default=None, type=int)
    get_part = AdditionalPartService.get_part(part_id)

    return current_app.response_class(
        response=json.dumps(get_part),
        status=200,
        mimetype='application/json'
    )


@add_part.route('/all_by_user', methods=['GET'])
def get_all_add_parts_by_user_from_database() -> Response:
    user_id = request.args.get('user_id', default=None, type=int)
    add_parts = AdditionalPartService.read_all_by_user_id(user_id)

    return current_app.response_class(
        response=json.dumps(add_parts),
        status=200,
        mimetype='application/json'
    )


@add_part.route('/all_by_table', methods=['GET'])
def get_all_add_parts_by_table_from_database() -> Response:
    table_id = request.args.get('table_id', default=None, type=int)
    add_parts = AdditionalPartService.read_all_by_table_id(table_id)

    return current_app.response_class(
        response=json.dumps(add_parts),
        status=200,
        mimetype='application/json'
    )


@add_part.route('/add', methods=['GET'])
def insert_add_part_in_database() -> Response:
    start = request.args.get('start', default=None, type=str)
    user_id = request.args.get('user_id', default=None, type=int)

    if start is None or user_id is None:
        return current_app.response_class(
            response=json.dumps({'error': 'No id or start creating part provided'}),
            status=400,
            mimetype='application/json'
        )

    success = AdditionalPartService.insert_part(start, user_id)

    if success:
        return current_app.response_class(
            response=json.dumps({'success': 'part added successfully'}),
            status=200,
            mimetype='application/json'
        )


@add_part.route('/update', methods=['GET'])
def update_table_in_database() -> Response:
    part_id = request.args.get('part_id', default=None, type=int)
    end = request.args.get('end', default=None, type=str)
    article = request.args.get('article', default=None, type=str)
    table_id = request.args.get('table_id', default=None, type=int)

    if (part_id is None or end is None or article is None
            or table_id is None):
        return current_app.response_class(
            response=json.dumps({'error': 'No all arg provided'}),
            status=400,
            mimetype='application/json'
        )

    success = AdditionalPartService.update_part(part_id, end, article, table_id)

    if success:
        return current_app.response_class(
            response=json.dumps({'success': 'part updated successfully'}),
            status=200,
            mimetype='application/json'
        )
