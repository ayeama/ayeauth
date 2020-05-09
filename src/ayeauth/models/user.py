from flask_login import UserMixin as BaseUserMixin

from ayeauth import db
from ayeauth.models import BaseModel


class UserMixin(BaseUserMixin):
    @property
    def is_active(self):
        return self.active

    def has_role(self):
        pass


class User(BaseModel, UserMixin):
    __tablename__ = "users"

    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship(
        "Role", secondary="user_roles", backref=db.backref("users", lazy="dynamic")
    )
