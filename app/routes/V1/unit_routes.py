from datetime import datetime, timezone
from typing import Sequence

import flask
from flask import Blueprint, Response, request, current_app, json

from app.database.enums import SurfaceType
from app.services import TableTopService, ColorPalletService, decode_image, save_image, UnitService

unit: flask.blueprints.Blueprint = Blueprint('unit', __name__)


@unit.route('/all', methods=['GET'])
def get_all_units_from_database() -> Response:
    units = UnitService.read_all()

    return current_app.response_class(
        response=json.dumps(units),
        status=200,
        mimetype='application/json'
    )


@unit.route('/add_table_top', methods=['POST'])
def add_table_top() -> Response:
    data = request.json
    up_id = data.get('up_id', None)

    if up_id is None:
        return current_app.response_class(
            response=json.dumps({'msg': 'No params provided'}),
            status=400,
            mimetype='application/json'
        )

    try:
        UnitService.insert(int(datetime.now(timezone.utc).timestamp() * 1000), up_id)

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


@unit.route('/get', methods=['GET'])
def get_unit_by_id() -> Response:
    unit_id = request.args.get('unit_id', default=None, type=int)
    get_unit = UnitService.get_by_id(unit_id)

    return current_app.response_class(
        response=json.dumps(get_unit),
        status=200,
        mimetype='application/json'
    )
