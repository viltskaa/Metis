import flask
from flask import Blueprint, Response, request, current_app, json

from app.services import TableTopPatternService

table_top_pattern: flask.blueprints.Blueprint = Blueprint('table_top_pattern', __name__)


@table_top_pattern.route('/all', methods=['GET'])
def get_all_table_tops_pattern_from_database() -> Response:
    table_tops = TableTopPatternService.read_all()

    return current_app.response_class(
        response=json.dumps(table_tops),
        status=200,
        mimetype='application/json'
    )


@table_top_pattern.route('/get', methods=['GET'])
def get_table_top_pattern_by_id() -> Response:
    ttp_id = request.args.get('ttp_id', default=None, type=int)
    get_top = TableTopPatternService.get_top_pattern(ttp_id)

    return current_app.response_class(
        response=json.dumps(get_top),
        status=200,
        mimetype='application/json'
    )


@table_top_pattern.route('/update', methods=['PATCH'])
def update_table_top_pattern_by_id() -> Response:
    ttp_id = request.args.get('ttp_id', default=None, type=int)
    article = request.args.get('article', default=None, type=str)
    name = request.args.get('name', default=None, type=str)
    material = request.args.get('material', default=None, type=str)

    if ttp_id is None or article is None or name is None or material is None:
        return current_app.response_class(
            response=json.dumps({'error': 'No all arg provided'}),
            status=400,
            mimetype='application/json'
        )

    get_ttp_id = TableTopPatternService.update_top_pattern(ttp_id, article, name, material)

    if get_ttp_id is not None:
        return current_app.response_class(
            response=json.dumps({'success': 'pattern updated successfully'}),
            status=200,
            mimetype='application/json'
        )
