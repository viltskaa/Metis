from flask import Blueprint

from .example_routes import example

V1_API_BLUEPRINT = Blueprint('v1', __name__)
V1_API_BLUEPRINT.register_blueprint(example, url_prefix=f"/{example.name}")
