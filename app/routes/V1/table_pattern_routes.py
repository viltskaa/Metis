import flask
from flask import Blueprint, Response, request, current_app, json

from app.services import decode_image, save_image, TablePatternService

table_pattern: flask.blueprints.Blueprint = Blueprint('table_pattern', __name__)


@table_pattern.route('/all', methods=['GET'])
def get_all_table_pattern() -> Response:
    tps = TablePatternService.read_all()

    return current_app.response_class(
        response=json.dumps(tps),
        status=200,
        mimetype='application/json'
    )


@table_pattern.route('/add', methods=['POST'])
def add_table_pattern() -> Response:
    data = request.json
    article = data.get('article', None)
    name = data.get('name', None)
    image_base64 = data.get("image_base64", None)
    ttp_id = data.get("ttp_id", None)

    if image_base64 is None or article is None or name is None or ttp_id is None:
        return current_app.response_class(
            response=json.dumps({'msg': 'No params provided'}),
            status=400,
            mimetype='application/json'
        )

    try:
        image = decode_image(image_base64)
        img_path = save_image(image)

        TablePatternService.insert(article, name, img_path, ttp_id)

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


@table_pattern.route('/get', methods=['GET'])
def get_tp_top_by_id() -> Response:
    table_pattern_id = request.args.get('table_pattern_id', default=None, type=int)
    get_tp = TablePatternService.read_by_id(table_pattern_id)

    return current_app.response_class(
        response=json.dumps(get_tp),
        status=200,
        mimetype='application/json'
    )


@table_pattern.route('/get', methods=['GET'])
def read_by_ttp_id() -> Response:
    table_top_pattern_id = request.args.get('table_top_pattern_id', default=None, type=int)
    get_tp = TablePatternService.read_by_ttp_id(table_top_pattern_id)

    return current_app.response_class(
        response=json.dumps(get_tp),
        status=200,
        mimetype='application/json'
    )