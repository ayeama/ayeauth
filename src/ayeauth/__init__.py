import uuid

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore

from ayeauth.config import Config

app = None
db = SQLAlchemy()
se = Security()


def _get_uuid():
    return str(uuid.uuid4())


def create():
    app = Flask(__name__)
    app.config.from_object(Config)

    from ayeauth.models.user import User
    from ayeauth.models.role import Role
    from ayeauth.models.user_role import UserRole  # noqa: F401

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)

    db.init_app(app)
    se.init_app(app, user_datastore)

    from ayeauth.users.routes import users_bp

    app.register_blueprint(users_bp, url_prefix="/users")

    return app
