import flask
from flask import Blueprint, Response, request, current_app, json

from app.services import TableService, UnitPatternTablePatternService

up_tp: flask.blueprints.Blueprint = Blueprint('up_tp', __name__)


@up_tp.route('/all', methods=['GET'])
def get_all_up_tps() -> Response:
    up_tps = UnitPatternTablePatternService.read_all()

    return current_app.response_class(
        response=json.dumps(up_tps),
        status=200,
        mimetype='application/json'
    )


@up_tp.route('/add', methods=['POST'])
def add_up_tp() -> Response:
    data = request.json
    table_pattern_id = data.get('table_pattern_id', None)
    unit_pattern_id = data.get('table_top_id', None)
    units_count = data.get('units_count', None)

    if table_pattern_id is None or unit_pattern_id is None or units_count is None:
        return current_app.response_class(
            response=json.dumps({'msg': 'No params provided'}),
            status=400,
            mimetype='application/json'
        )

    try:
        UnitPatternTablePatternService.insert(table_pattern_id, unit_pattern_id, units_count)

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


@up_tp.route('/get', methods=['GET'])
def get_up_tp_by_id() -> Response:
    up_tp_id = request.args.get('up_tp_id', default=None, type=int)
    get_up_tp = UnitPatternTablePatternService.read_by_id(up_tp_id)

    return current_app.response_class(
        response=json.dumps(get_up_tp),
        status=200,
        mimetype='application/json'
    )


@up_tp.route('/get_by_up_id', methods=['GET'])
def read_by_up_id() -> Response:
    unit_pattern_id = request.args.get('unit_pattern_id', default=None, type=int)
    get_up_tp = UnitPatternTablePatternService.read_by_up_id(unit_pattern_id)

    return current_app.response_class(
        response=json.dumps(get_up_tp),
        status=200,
        mimetype='application/json'
    )


@up_tp.route('/get_by_tp_id', methods=['GET'])
def read_by_tp_id() -> Response:
    table_pattern_id = request.args.get('table_pattern_id', default=None, type=int)
    get_up_tp = UnitPatternTablePatternService.read_by_tp_id(table_pattern_id)

    return current_app.response_class(
        response=json.dumps(get_up_tp),
        status=200,
        mimetype='application/json'
    )
