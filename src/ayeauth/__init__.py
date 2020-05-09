from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore

from ayeauth.config import Config

app = None
db = SQLAlchemy()
se = Security()


def create():
    app = Flask(__name__)
    app.config.from_object(Config)

    from ayeauth.users.models import User, Role
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)

    db.init_app(app)
    se.init_app(app, user_datastore)

    from ayeauth.users.routes import users_bp

    app.register_blueprint(users_bp, url_prefix='/users')

    return app
