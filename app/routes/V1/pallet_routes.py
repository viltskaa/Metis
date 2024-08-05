import flask
from flask import Blueprint, Response, request, current_app, json

from app.services import PalletService

pallet: flask.blueprints.Blueprint = Blueprint('pallet', __name__)


@pallet.route('/all', methods=['GET'])
def get_all_pallet_from_database() -> Response:
    pallets = PalletService.read_all()

    return current_app.response_class(
        response=json.dumps(pallets),
        status=200,
        mimetype='application/json'
    )


@pallet.route('/get', methods=['GET'])
def get_pallet_by_id() -> Response:
    pallet_id = request.args.get('pallet_id', default=None, type=int)
    get_pallet = PalletService.get_pallet(pallet_id)

    return current_app.response_class(
        response=json.dumps(get_pallet),
        status=200,
        mimetype='application/json'
    )


@pallet.route('/all_by_table', methods=['GET'])
def get_all_tables_by_table_from_database() -> Response:
    table_id = request.args.get('table_id', default=None, type=int)
    pallets = PalletService.read_all_by_table_id(table_id)

    return current_app.response_class(
        response=json.dumps(pallets),
        status=200,
        mimetype='application/json'
    )


@pallet.route('/all_by_table_and_surface', methods=['GET'])
def get_all_tables_by_table_and_surface_from_database() -> Response:
    table_id = request.args.get('table_id', default=None, type=int)
    surface = request.args.get('surface', default=None, type=int)
    pallets = PalletService.read_all_by_table_id_and_surface(table_id, surface)

    return current_app.response_class(
        response=json.dumps(pallets),
        status=200,
        mimetype='application/json'
    )


@pallet.route('/add', methods=['GET'])
def insert_pallet_in_database() -> Response:
    hex_color = request.args.get('hex_color', default=None, type=str)
    table_id = request.args.get('table_id', default=None, type=int)
    surface = request.args.get('surface', default=None, type=int)

    if hex_color is None or table_id is None or surface is None:
        return current_app.response_class(
            response=json.dumps({'error': 'No id, color or surface pallet provided'}),
            status=400,
            mimetype='application/json'
        )

    success = PalletService.insert_pallet(hex_color, table_id, surface)

    if success:
        return current_app.response_class(
            response=json.dumps({'success': 'pallet added successfully'}),
            status=200,
            mimetype='application/json'
        )
