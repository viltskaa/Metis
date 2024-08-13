import flask
from flask import Blueprint, Response, request, current_app, json

from app.services import TableTopService

table_top: flask.blueprints.Blueprint = Blueprint('table_top', __name__)


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
