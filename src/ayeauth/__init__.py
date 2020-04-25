from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from ayeauth.config import Config

db = SQLAlchemy()


def create():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from ayeauth.users.routes import users_bp

    app.register_blueprint(users_bp, url_prefix='/users')

    return app
