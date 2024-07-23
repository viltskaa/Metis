import flask
from flask import Blueprint, Response, request, current_app, json

from app.services import TableService

table: flask.blueprints.Blueprint = Blueprint('table', __name__)


@table.route('/all', methods=['GET'])
def get_all_tables_from_database() -> Response:
    tables = TableService.read_all()

    return current_app.response_class(
        response=json.dumps(tables),
        status=200,
        mimetype='application/json'
    )


@table.route('/get', methods=['GET'])
def get_table_by_id() -> Response:
    table_id = request.args.get('table_id', default=None, type=int)
    get_table = TableService.get_table(table_id)

    return current_app.response_class(
        response=json.dumps(get_table),
        status=200,
        mimetype='application/json'
    )


@table.route('/all_by_user', methods=['GET'])
def get_all_tables_by_user_from_database() -> Response:
    user_id = request.args.get('user_id', default=None, type=int)
    tables = TableService.read_all_by_user_id(user_id)

    return current_app.response_class(
        response=json.dumps(tables),
        status=200,
        mimetype='application/json'
    )


@table.route('/add', methods=['GET'])
def insert_table_in_database() -> Response:
    start = request.args.get('start', default=None, type=str)
    user_id = request.args.get('user_id', default=None, type=int)

    if start is None or user_id is None:
        return current_app.response_class(
            response=json.dumps({'error': 'No id or start creating table provided'}),
            status=400,
            mimetype='application/json'
        )

    success = TableService.insert_table(start, user_id)

    if success:
        return current_app.response_class(
            response=json.dumps({'success': 'table added successfully'}),
            status=200,
            mimetype='application/json'
        )


@table.route('/update', methods=['GET'])
def update_table_in_database() -> Response:
    table_id = request.args.get('table_id', default=None, type=int)
    article = request.args.get('article', default=None, type=str)
    qr_code = request.args.get('qr_code', default=None, type=str)
    top_id = request.args.get('top_id', default=None, type=int)
    marketplace_id = request.args.get('marketplace_id', default=None, type=int)
    end = request.args.get('end', default=None, type=str)

    if (table_id is None or article is None or qr_code is None
            or top_id is None or marketplace_id is None or end is None):
        return current_app.response_class(
            response=json.dumps({'error': 'No all arg provided'}),
            status=400,
            mimetype='application/json'
        )

    success = TableService.update_table(table_id, article, qr_code,
                                        top_id, marketplace_id, end)

    if success:
        return current_app.response_class(
            response=json.dumps({'success': 'table updated successfully'}),
            status=200,
            mimetype='application/json'
        )
