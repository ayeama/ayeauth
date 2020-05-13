from flask_login import UserMixin as BaseUserMixin

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
    active = db.Column(db.Boolean())
    roles = db.relationship(
        "Role", secondary="user_roles", backref=db.backref("users", lazy="dynamic")
    )

    def __init__(self, username, password):
        super(User, self).__init__()

        self.username = username
        self.password = hash_password(password)

    def __repr__(self):
        return str(self.id)

    def __str__(self):
        return str(self.username)
