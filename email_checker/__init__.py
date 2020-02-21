from flask import Flask
from config import config_map
from flask_wtf import CSRFProtect
from email_checker.utils.commons import ReConverter


def create_app(config_name):
    app = Flask(__name__)
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)
    CSRFProtect(app)
    app.url_map.converters["re"] = ReConverter

    from email_checker import api_1_0
    app.register_blueprint(api_1_0.api, url_prefix="/api/v1.0")

    from email_checker import web_html
    app.register_blueprint(web_html.html)
    return app

