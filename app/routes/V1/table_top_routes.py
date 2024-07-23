import flask
from flask import Blueprint, Response, request, current_app, json

from app.services import TableTopService

table_top: flask.blueprints.Blueprint = Blueprint('table_top', __name__)


@table_top.route('/all_by_user', methods=['GET'])
def get_all_table_tops_by_user_from_database() -> Response:
    user_id = request.args.get('user_id', default=None, type=int)
    table_tops = TableTopService.read_all_by_user_id(user_id)

    return current_app.response_class(
        response=json.dumps(table_tops),
        status=200,
        mimetype='application/json'
    )


@table_top.route('/all', methods=['GET'])
def get_all_table_tops_from_database() -> Response:
    table_tops = TableTopService.read_all()

    return current_app.response_class(
        response=json.dumps(table_tops),
        status=200,
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


@table_top.route('/add', methods=['GET'])
def insert_table_top_in_database() -> Response:
    start = request.args.get('start', default=None, type=str)
    user_id = request.args.get('user_id', default=None, type=int)

    if start is None or user_id is None:
        return current_app.response_class(
            response=json.dumps({'error': 'No id or start creating top provided'}),
            status=400,
            mimetype='application/json'
        )

    success = TableTopService.insert_top(start, user_id)

    if success:
        return current_app.response_class(
            response=json.dumps({'success': 'top added successfully'}),
            status=200,
            mimetype='application/json'
        )


@table_top.route('/update', methods=['GET'])
def update_table_top_in_database() -> Response:
    top_id = request.args.get('top_id', default=None, type=int)
    width = request.args.get('width', default=None, type=float)
    height = request.args.get('height', default=None, type=float)
    perimeter = request.args.get('perimeter', default=None, type=float)
    depth = request.args.get('depth', default=None, type=float)
    color_main = request.args.get('color_main', default=None, type=str)
    color_edge = request.args.get('color_edge', default=None, type=str)
    material = request.args.get('material', default=None, type=str)
    article = request.args.get('article', default=None, type=str)
    end = request.args.get('end', default=None, type=str)

    if (top_id is None or width is None or height is None
            or perimeter is None or depth is None or color_main is None
            or color_edge is None or material is None or article is None
            or end is None):
        return current_app.response_class(
            response=json.dumps({'error': 'No all arg provided'}),
            status=400,
            mimetype='application/json'
        )

    success = TableTopService.update_top(top_id, width, height,
                                         perimeter, depth, color_main,
                                         color_edge, material, article, end)

    if success:
        return current_app.response_class(
            response=json.dumps({'success': 'top updated successfully'}),
            status=200,
            mimetype='application/json'
        )
