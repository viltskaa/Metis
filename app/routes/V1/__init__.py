from flask import Blueprint

from .table_top_routes import table_top
from .android_routes import android
from .table_top_pattern_routes import table_top_pattern
from .color_pallet_routes import color_pallet
from .color_pallet_pattern_routes import color_pallet_pattern
from .auth_routes import auth

V1_API_BLUEPRINT = Blueprint('v1', __name__)
V1_API_BLUEPRINT.register_blueprint(table_top, url_prefix=f"/{table_top.name}")
V1_API_BLUEPRINT.register_blueprint(android, url_prefix=f"/{android.name}")
V1_API_BLUEPRINT.register_blueprint(table_top_pattern, url_prefix=f"/{table_top_pattern.name}")
V1_API_BLUEPRINT.register_blueprint(color_pallet, url_prefix=f"/{color_pallet.name}")
V1_API_BLUEPRINT.register_blueprint(color_pallet_pattern, url_prefix=f"/{color_pallet_pattern.name}")
V1_API_BLUEPRINT.register_blueprint(auth, url_prefix=f"/{auth.name}")
