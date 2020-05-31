from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_principal import Principal, identity_loaded

from ayeauth.config import Config

app = None
db = SQLAlchemy()
lm = LoginManager()
pr = Principal()


def create():
    app = Flask(__name__)
    app.config.from_object(Config)

    from ayeauth.loader import (
        user_loader,
        # request_loader,
        identity_loader,
        on_identity_loaded,
        unauthorized_handler,
    )
    from ayeauth.models.user import AnonymousUser

    lm.login_view = "auth_bp.login"
    lm.anonymous_user = AnonymousUser
    lm.user_loader(user_loader)
    # lm.request_loader(request_loader)
    lm.unauthorized_handler(unauthorized_handler)
    pr.identity_loader(identity_loader)

    db.init_app(app)
    lm.init_app(app)
    pr.init_app(app)

    identity_loaded.connect_via(app)(on_identity_loaded)

    from ayeauth.models.user import User  # noqa: F401
    from ayeauth.models.role import Role  # noqa: F401
    from ayeauth.models.user_role import UserRole  # noqa: F401
    from ayeauth.models.user_authorized_application import (  # noqa: F401
        UserAuthorizedApplication,
    )
    from ayeauth.models.application import Application  # noqa: F401
    from ayeauth.models.scope import Scope  # noqa: F401
    from ayeauth.models.application_scope import ApplicationScope  # noqa: F401
    from ayeauth.models.authorization_code import AuthorizationCode  # noqa: F401

    from ayeauth.home.routes import home_bp
    from ayeauth.auth.routes import auth_bp
    from ayeauth.oauth.routes import oauth_bp
    from ayeauth.user.routes import user_bp
    from ayeauth.application.routes import application_bp

    app.register_blueprint(home_bp, url_prefix="/")
    app.register_blueprint(auth_bp, url_prefix="/")
    app.register_blueprint(oauth_bp, url_prefix="/oauth")
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(application_bp, url_prefix="/application")

    return app
