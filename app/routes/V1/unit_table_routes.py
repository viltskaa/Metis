import flask
from flask import Blueprint, Response, request, current_app, json

from app.services import TableService, UnitPatternTablePatternService, UnitTableService

unit_table: flask.blueprints.Blueprint = Blueprint('unit_table', __name__)


@unit_table.route('/all', methods=['GET'])
def get_all_up_tps() -> Response:
    uts = UnitTableService.read_all()

    return current_app.response_class(
        response=json.dumps(uts),
        status=200,
        mimetype='application/json'
    )


@unit_table.route('/add', methods=['POST'])
def add_ut() -> Response:
    data = request.json
    table_id = data.get('table_id', None)
    unit_id = data.get('unit_id', None)

    if table_id is None or unit_id is None:
        return current_app.response_class(
            response=json.dumps({'msg': 'No params provided'}),
            status=400,
            mimetype='application/json'
        )

    try:
        UnitTableService.insert(table_id, unit_id)

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


@unit_table.route('/get', methods=['GET'])
def get_up_tp_by_id() -> Response:
    ut_id = request.args.get('ut_id', default=None, type=int)
    get_ut = UnitTableService.read_by_id(ut_id)

    return current_app.response_class(
        response=json.dumps(get_ut),
        status=200,
        mimetype='application/json'
    )


@unit_table.route('/get_by_table_id', methods=['GET'])
def read_by_table_id() -> Response:
    table_id = request.args.get('table_id', default=None, type=int)
    get_ut = UnitTableService.read_by_table_id(table_id)

    return current_app.response_class(
        response=json.dumps(get_ut),
        status=200,
        mimetype='application/json'
    )


@unit_table.route('/get_by_unit_id', methods=['GET'])
def read_by_unit_id() -> Response:
    unit_id = request.args.get('unit_id', default=None, type=int)
    get_ut = UnitTableService.read_by_unit_id(unit_id)

    return current_app.response_class(
        response=json.dumps(get_ut),
        status=200,
        mimetype='application/json'
    )
