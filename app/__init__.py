from flask import Flask, render_template
from config import config

def create_app(config_name: str) -> Flask:
    '''Configuration name'''
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .flask_extensions import extensions_all
    for extension in extensions_all:
        extension.init_app(app)

    from .views import blueprints_all
    for blueprint in blueprints_all:
        app.register_blueprint(blueprint)

    return app
