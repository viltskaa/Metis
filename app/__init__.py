from flask import Flask

from config import DevelopConfig
from .routes import ROUTES
from .utils import pre


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopConfig)

    for route in ROUTES:
        app.register_blueprint(route, url_prefix=f"/{route.name}")

    try:
        from .database import database
        database.init_app(app)
    except Exception as e:
        app.logger.error(e)

    if app.debug:
        @app.route('/routes')
        def route():
            return pre("<br/>".join(
                [f"{url.endpoint:50} | {url.rule:20} | {url.methods}" for url in app.url_map.iter_rules()]
            ))

    return app
