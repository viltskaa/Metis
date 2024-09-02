from datetime import datetime, timezone
from typing import Sequence

import flask
from flask import Blueprint, Response, request, current_app, json

from app.database.enums import SurfaceType
from app.services import TableTopService, ColorPalletService
from cv import decode_image, save_image

table_top: flask.blueprints.Blueprint = Blueprint('table_top', __name__)


@table_top.route('/all', methods=['GET'])
def get_all_table_tops_from_database() -> Response:
    table_tops = TableTopService.read_all()

    return current_app.response_class(
        response=json.dumps(table_tops),
        status=200,
        mimetype='application/json'
    )


@table_top.route('/add_table_top', methods=['POST'])
def add_table_top() -> Response:
    data = request.json
    ttp_id = data.get('ttp_id', default=None, type=int)
    perimeter = data.get('perimeter', default=None, type=float)
    width = data.get('width', default=None, type=float)
    height = data.get('height', default=None, type=float)
    image_base64 = data.get("image_base64", default=None, type=str)
    colors = data.get("colors", default=None, type=Sequence[Sequence[int]])

    if image_base64 is None or colors is None or height is None or width is None \
            or perimeter is None or ttp_id is None:
        return current_app.response_class(
            response=json.dumps({'error': 'No params provided'}),
            status=400,
            mimetype='application/json'
        )

    try:
        image = decode_image(image_base64)
        img_path = save_image(image)

        tt_id = TableTopService.insert_top(int(datetime.now(timezone.utc).timestamp() * 1000),
                                           width,
                                           height,
                                           perimeter,
                                           img_path,
                                           ttp_id
                                           )

        success = ColorPalletService.insert_all_cp(SurfaceType.MAIN.value, colors, tt_id)

        if success:
            return current_app.response_class(
                response=json.dumps({'success': 'Data added successfully'}),
                status=200,
                mimetype='application/json'
            )

    except Exception as e:
        print(f"Exception occurred: {e.with_traceback()}")
        return current_app.response_class(
            response=json.dumps({'error': 'An error occurred during insert'}),
            status=500,
            mimetype='application/json'
        )


@table_top.route('/get', methods=['GET'])
def get_table_top_by_id() -> Response:
    top_id = request.args.get('top_id', default=None, type=int)
    get_top = TableTopService.get_top(top_id)

    return current_app.response_class(
        response=json.dumps(get_top),
        status=200,
        mimetype='application/json'
    )
