import flask
from flask import Blueprint, Response, request, current_app, json

from app.services import ColorPalletPatternService

color_pallet_pattern: flask.blueprints.Blueprint = Blueprint('color_pallet_pattern', __name__)


@color_pallet_pattern.route('/all', methods=['GET'])
def get_all_color_pallet_patterns_from_database() -> Response:
    color_pallets = ColorPalletPatternService.read_all()

    return current_app.response_class(
        response=json.dumps(color_pallets),
        status=200,
        mimetype='application/json'
    )


@color_pallet_pattern.route('/all_by_tt_id', methods=['GET'])
def get_all_color_pallet_patterns_from_database_by_ttp_id() -> Response:
    ttp_id = request.args.get('ttp_id', default=None, type=int)
    color_pallets = ColorPalletPatternService.read_all_by_ttp_id(ttp_id)

    return current_app.response_class(
        response=json.dumps(color_pallets),
        status=200,
        mimetype='application/json'
    )


@color_pallet_pattern.route('/get', methods=['GET'])
def get_color_pallet_pattern_by_id() -> Response:
    cpp_id = request.args.get('cp_id', default=None, type=int)
    get_cp = ColorPalletPatternService.get_cpp(cpp_id)

    return current_app.response_class(
        response=json.dumps(get_cp),
        status=200,
        mimetype='application/json'
    )
