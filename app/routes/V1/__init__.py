from flask import Blueprint

from .table_top_routes import table_top
from .android_routes import android

V1_API_BLUEPRINT = Blueprint('v1', __name__)
V1_API_BLUEPRINT.register_blueprint(table_top, url_prefix=f"/{table_top.name}")
V1_API_BLUEPRINT.register_blueprint(android, url_prefix=f"/{android.name}")
