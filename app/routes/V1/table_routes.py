from datetime import datetime, timezone

import flask
from flask import Blueprint, Response, request, current_app, json

from app.services import decode_image, save_image, TablePatternService, TableService

tables: flask.blueprints.Blueprint = Blueprint('tables', __name__)


@tables.route('/all', methods=['GET'])
def get_all_tables() -> Response:
    tables = TableService.read_all()

    return current_app.response_class(
        response=json.dumps(tables),
        status=200,
        mimetype='application/json'
    )


@tables.route('/add', methods=['POST'])
def add_table_pattern() -> Response:
    data = request.json
    table_pattern_id = data.get('table_pattern_id', None)
    table_top_id = data.get('table_top_id', None)

    if table_top_id is None or table_pattern_id is None:
        return current_app.response_class(
            response=json.dumps({'msg': 'No params provided'}),
            status=400,
            mimetype='application/json'
        )

    try:
        TableService.insert(table_pattern_id, int(datetime.now(timezone.utc).timestamp() * 1000), table_top_id)

        return current_app.response_class(
            response=json.dumps({'msg': 'Data added successfully'}),
            status=200,
            mimetype='application/json'
        )

    except Exception as e:
        print(f"Exception occurred: {e.with_traceback()}")
        return current_app.response_class(
            response=json.dumps({'msg': 'An error occurred during insert'}),
            status=500,
            mimetype='application/json'
        )


@tables.route('/get', methods=['GET'])
def get_table_by_id() -> Response:
    table_id = request.args.get('table_id', default=None, type=int)
    get_table = TableService.read_by_id(table_id)

    return current_app.response_class(
        response=json.dumps(get_table),
        status=200,
        mimetype='application/json'
    )


@tables.route('/get_by_tt_id', methods=['GET'])
def read_by_tt_id() -> Response:
    table_top_id = request.args.get('table_top_id', default=None, type=int)
    get_table = TableService.read_by_tt_id(table_top_id)

    return current_app.response_class(
        response=json.dumps(get_table),
        status=200,
        mimetype='application/json'
    )

@tables.route('/get_by_tp_id', methods=['GET'])
def read_by_tp_id() -> Response:
    table_pattern_id = request.args.get('table_pattern_id', default=None, type=int)
    get_table = TableService.read_by_tp_id(table_pattern_id)

    return current_app.response_class(
        response=json.dumps(get_table),
        status=200,
        mimetype='application/json'
    )
