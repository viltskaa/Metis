import flask
from flask import Blueprint, Response, request, current_app, json

from app.services import WorkService

work: flask.blueprints.Blueprint = Blueprint('work', __name__)


@work.route('/all', methods=['GET'])
def get_all_works_from_database() -> Response:
    works = WorkService.read_all()

    return current_app.response_class(
        response=json.dumps(works),
        status=200,
        mimetype='application/json'
    )


@work.route('/all_by_user', methods=['GET'])
def get_all_works_by_user_from_database() -> Response:
    user_id = request.args.get('user_id', default=None, type=int)
    works = WorkService.read_all_by_user_id(user_id)

    return current_app.response_class(
        response=json.dumps(works),
        status=200,
        mimetype='application/json'
    )


@work.route('/get', methods=['GET'])
def get_work_by_id() -> Response:
    work_id = request.args.get('work_id', default=None, type=int)
    get_work = WorkService.get_work(work_id)

    return current_app.response_class(
        response=json.dumps(get_work),
        status=200,
        mimetype='application/json'
    )


@work.route('/add', methods=['GET'])
def insert_work_in_database() -> Response:
    work_start = request.args.get('work_start', default=None, type=str)
    user_id = request.args.get('user_id', default=None, type=int)

    if work_start is None or user_id is None:
        return current_app.response_class(
            response=json.dumps({'error': 'No id or start work provided'}),
            status=400,
            mimetype='application/json'
        )

    success = WorkService.insert_work(work_start, user_id)

    if success:
        return current_app.response_class(
            response=json.dumps({'success': 'work added successfully'}),
            status=200,
            mimetype='application/json'
        )


@work.route('/update', methods=['GET'])
def update_work_in_database() -> Response:
    work_end = request.args.get('work_end', default=None, type=str)
    work_id = request.args.get('work_id', default=None, type=int)

    if work_end is None or work_id is None:
        return current_app.response_class(
            response=json.dumps({'error': 'No id or end work provided'}),
            status=400,
            mimetype='application/json'
        )

    success = WorkService.update_work(work_end, work_id)

    if success:
        return current_app.response_class(
            response=json.dumps({'success': 'work updated successfully'}),
            status=200,
            mimetype='application/json'
        )
