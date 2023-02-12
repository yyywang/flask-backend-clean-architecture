# -*- coding: utf-8 -*-
"""
  Created by 怀月 on 2023/1/12.
"""
from flask import Flask
from app.config import setting
from app.models import db


def create_app() -> Flask:
    app = Flask(__name__)

    app.config.from_object(setting)
    register_blueprints(app)
    configure_db(app)

    return app


def register_blueprints(app: Flask):
    from app.api.v1 import create_v1

    app.register_blueprint(create_v1(), url_prefix="/api/v1")


def configure_db(app: Flask):
    db.init_app(app)

    with app.app_context():
        db.create_all()
