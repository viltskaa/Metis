from flask import json, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.database.enums import WorkerType
from app.repositories import WorkerRepository


def role_required(*roles: WorkerType):
    def decorator(func):
        @jwt_required()
        def wrapper(*args, **kwargs):
            user_id = get_jwt_identity()
            worker = WorkerRepository.get_by_id(user_id)
            if worker and worker['type'] in roles:
                return func(*args, **kwargs)
            else:
                return current_app.response_class(
                    response=json.dumps({"msg": "Access forbidden: insufficient permissions"}),
                    status=403,
                    mimetype='application/json'
                )

        return wrapper

    return decorator
