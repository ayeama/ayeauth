import uuid

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_principal import Principal, identity_loaded

from ayeauth.config import Config

app = None
db = SQLAlchemy()
lm = LoginManager()
pr = Principal()


def _get_uuid():
    return str(uuid.uuid4())


def create():
    app = Flask(__name__)
    app.config.from_object(Config)

    from ayeauth.auth.loader import (
        user_loader,
        request_loader,
        identity_loader,
        on_identity_loaded,
        unauthorized_handler,
    )
    from ayeauth.models.user import AnonymousUser

    lm.login_view = "auth_bp.login"
    lm.anonymous_user = AnonymousUser
    lm.user_loader(user_loader)
    lm.request_loader(request_loader)
    lm.unauthorized_handler(unauthorized_handler)
    pr.identity_loader(identity_loader)

    db.init_app(app)
    lm.init_app(app)
    pr.init_app(app)

    identity_loaded.connect_via(app)(on_identity_loaded)

    from ayeauth.models.user import User  # noqa: F401
    from ayeauth.models.role import Role  # noqa: F401
    from ayeauth.models.user_role import UserRole  # noqa: F401

    from ayeauth.home.routes import home_bp
    from ayeauth.auth.routes import auth_bp
    from ayeauth.users.routes import users_bp

    app.register_blueprint(home_bp, url_prefix="/")
    app.register_blueprint(auth_bp, url_prefix="/")
    app.register_blueprint(users_bp, url_prefix="/users")

    return app
