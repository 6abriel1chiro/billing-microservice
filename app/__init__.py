import config
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    # Configure your app here

    environment_configuration = os.environ["CONFIGURATION_SETUP"]
    app.config.from_object(environment_configuration)

    db.init_app(app)
    with app.app_context():
        from billing_api import billing_api_blueprint

        app.register_blueprint(billing_api_blueprint)
        return app
