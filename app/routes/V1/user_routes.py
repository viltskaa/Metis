import flask
from flask import Blueprint, Response, request, current_app, json

from app.services import UserService

user: flask.blueprints.Blueprint = Blueprint('user', __name__)


@user.route('/all', methods=['GET'])
def get_all_users_from_database() -> Response:
    users = UserService.read_all()

    return current_app.response_class(
        response=json.dumps(users),
        status=200,
        mimetype='application/json'
    )


@user.route('/get', methods=['GET'])
def get_user_by_id() -> Response:
    user_id = request.args.get('user_id', default=None, type=int)
    get_user = UserService.get_user(user_id)

    return current_app.response_class(
        response=json.dumps(get_user),
        status=200,
        mimetype='application/json'
    )


@user.route('/add', methods=['GET'])
def insert_user_in_database() -> Response:
    name = request.args.get('name', default=None, type=str)

    if name is None:
        return current_app.response_class(
            response=json.dumps({'error': 'No name provided'}),
            status=400,
            mimetype='application/json'
        )

    success = UserService.insert_user(name)

    if success:
        return current_app.response_class(
            response=json.dumps({'success': 'user added successfully'}),
            status=200,
            mimetype='application/json'
        )
