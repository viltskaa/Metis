import flask
from flask import Blueprint, Response, request, current_app, json

from app.database.enums import UnitType
from app.services import decode_image, save_image, UnitPatternService

unit_pattern: flask.blueprints.Blueprint = Blueprint('unit_pattern', __name__)


@unit_pattern.route('/all', methods=['GET'])
def get_all_units_pastern_from_database() -> Response:
    units = UnitPatternService.read_all()

    return current_app.response_class(
        response=json.dumps(units),
        status=200,
        mimetype='application/json'
    )


@unit_pattern.route('/add_unit_pattern', methods=['POST'])
def add_unit_pattern() -> Response:
    data = request.json
    article = data.get('article', None)
    name = data.get('name', None)
    image_base64 = data.get('image_path', None)
    unit_type = data.get('unit_type', None)

    if article is None or name is None or image_base64 is None or unit_type is None:
        return current_app.response_class(
            response=json.dumps({'msg': 'No params provided'}),
            status=400,
            mimetype='application/json'
        )

    try:
        image = decode_image(image_base64)
        img_path = save_image(image)

        UnitPatternService.insert(article, name, img_path, UnitType(unit_type))

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


@unit_pattern.route('/get', methods=['GET'])
def read_by_id() -> Response:
    up_id = request.args.get('up_id', default=None, type=int)
    get_up = UnitPatternService.read_by_id(up_id)

    return current_app.response_class(
        response=json.dumps(get_up),
        status=200,
        mimetype='application/json'
    )
