import os

from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine
from bloxs.infra.controller.account_controller import account_controller
from bloxs.infra.controller.auth_controller import auth_controller
from bloxs.infra.controller.transaction_controller import transaction_controller
from bloxs.infra.DI.injector_factory import InjectorFactory

DB_URL = os.environ["DB_URL"]


def create_app():
    app = Flask(__name__)
    CORS(app)
    engine = create_engine(DB_URL)
    InjectorFactory().init(engine)
    app.register_blueprint(auth_controller)
    app.register_blueprint(account_controller)
    app.register_blueprint(transaction_controller)
    return app


if __name__ == "__main__":
    create_app().run("0.0.0.0", 5000)
