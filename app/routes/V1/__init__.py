from flask import Blueprint

from .table_top_routes import table_top
from .android_routes import android
from .table_top_pattern_routes import table_top_pattern
from .color_pallet_routes import color_pallet
from .color_pallet_pattern_routes import color_pallet_pattern
from .auth_routes import auth
from .unit_pattern_routes import unit_pattern
from .table_routes import tables
from .unit_pattern_table_pattern_routes import up_tp
from .unit_table_routes import unit_table
from .table_pattern_routes import table_pattern

V1_API_BLUEPRINT = Blueprint('v1', __name__)
V1_API_BLUEPRINT.register_blueprint(table_top, url_prefix=f"/{table_top.name}")
V1_API_BLUEPRINT.register_blueprint(android, url_prefix=f"/{android.name}")
V1_API_BLUEPRINT.register_blueprint(table_top_pattern, url_prefix=f"/{table_top_pattern.name}")
V1_API_BLUEPRINT.register_blueprint(color_pallet, url_prefix=f"/{color_pallet.name}")
V1_API_BLUEPRINT.register_blueprint(color_pallet_pattern, url_prefix=f"/{color_pallet_pattern.name}")
V1_API_BLUEPRINT.register_blueprint(auth, url_prefix=f"/{auth.name}")
V1_API_BLUEPRINT.register_blueprint(unit_pattern, url_prefix=f"/{unit_pattern.name}")
V1_API_BLUEPRINT.register_blueprint(tables, url_prefix=f"/{tables.name}")
V1_API_BLUEPRINT.register_blueprint(up_tp, url_prefix=f"/{up_tp.name}")
V1_API_BLUEPRINT.register_blueprint(unit_table, url_prefix=f"/{unit_table.name}")
V1_API_BLUEPRINT.register_blueprint(table_pattern, url_prefix=f"/{table_pattern.name}")