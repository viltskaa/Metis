import flask
from flask import Blueprint, Response, request, current_app, json

from app.services import ColorPalletService

color_pallet: flask.blueprints.Blueprint = Blueprint('color_pallet', __name__)


@color_pallet.route('/all', methods=['GET'])
def get_all_color_pallets_from_database() -> Response:
    color_pallets = ColorPalletService.read_all()

    return current_app.response_class(
        response=json.dumps(color_pallets),
        status=200,
        mimetype='application/json'
    )


@color_pallet.route('/all_by_tt_id', methods=['GET'])
def get_all_color_pallets_from_database_by_tt_id() -> Response:
    tt_id = request.args.get('tt_id', default=None, type=int)
    color_pallets = ColorPalletService.read_all_by_tt_id(tt_id)

    return current_app.response_class(
        response=json.dumps(color_pallets),
        status=200,
        mimetype='application/json'
    )


@color_pallet.route('/get', methods=['GET'])
def get_color_pallet_by_id() -> Response:
    cp_id = request.args.get('cp_id', default=None, type=int)
    get_cp = ColorPalletService.get_cp(cp_id)

    return current_app.response_class(
        response=json.dumps(get_cp),
        status=200,
        mimetype='application/json'
    )
