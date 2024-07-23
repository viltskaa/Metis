from flask import Blueprint

from .example_routes import example
from .user_routes import user
from .work_routes import work
from .table_top_routes import table_top
from .table_routes import table
from .additional_part_routes import add_part

V1_API_BLUEPRINT = Blueprint('v1', __name__)
V1_API_BLUEPRINT.register_blueprint(example, url_prefix=f"/{example.name}")
V1_API_BLUEPRINT.register_blueprint(user, url_prefix=f"/{user.name}")
V1_API_BLUEPRINT.register_blueprint(work, url_prefix=f"/{work.name}")
V1_API_BLUEPRINT.register_blueprint(table_top, url_prefix=f"/{table_top.name}")
V1_API_BLUEPRINT.register_blueprint(table, url_prefix=f"/{table.name}")
V1_API_BLUEPRINT.register_blueprint(add_part, url_prefix=f"/{add_part.name}")
