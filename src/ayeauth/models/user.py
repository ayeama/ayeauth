from flask_login import AnonymousUserMixin
from flask_login import UserMixin as BaseUserMixin
from werkzeug.datastructures import ImmutableList

from ayeauth import db
from ayeauth.auth.password import hash_password
from ayeauth.models import BaseModel


class UserMixin(BaseUserMixin):
    @property
    def is_active(self):
        return self.active

    def has_role(self, role):
        if role in self.roles:
            return True
        return False


class User(BaseModel, UserMixin):
    __tablename__ = "users"

    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), default=True)
    roles = db.relationship(
        "Role", secondary="user_roles", backref=db.backref("users", lazy="dynamic")
    )
    owned_applications = db.relationship("Application", backref="owner")
    authorized_applications = db.relationship(
        "Application",
        secondary="user_authorized_applications",
        backref=db.backref("users", lazy="dynamic"),
    )

    def __init__(self, username, password):
        super(User, self).__init__()

        self.username = username
        self.password = hash_password(password)

    def __str__(self):
        return str(self.username)


class AnonymousUser(AnonymousUserMixin):
    def __init__(self):
        self.roles = ImmutableList()

    def has_role(self, *args):
        return False
