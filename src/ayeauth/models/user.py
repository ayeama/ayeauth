from flask_login import UserMixin as BaseUserMixin
from flask_security.utils import hash_password

from ayeauth import db
from ayeauth.models import BaseDatastore, BaseModel


class UserMixin(BaseUserMixin):
    @property
    def is_active(self):
        return self.active

    def has_role(self):
        pass


class User(BaseModel, UserMixin):
    __tablename__ = "users"

    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean())
    roles = db.relationship(
        "Role", secondary="user_roles", backref=db.backref("users", lazy="dynamic")
    )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.username})"

    def __str__(self):
        return f"{self.__class__.__name__}({self.id}, {self.username})"


class UserDatastore(BaseDatastore):
    def get(self, many=False, **kwargs):
        if many:
            return User.query.all()
        return User.query.filter_by(**kwargs).first()

    def post(self, **kwargs):
        if kwargs.get("password", None) is not None:
            kwargs["password"] = hash_password(kwargs["password"])

        user = User(**kwargs)
        db.session.add(user)
        db.session.commit()

    def put(self, _id, **kwargs):
        user = self.get(id=_id)
        for key, value in kwargs.items():
            setattr(user, key, value)
        db.session.commit()

    def delete(self, _id):
        user = self.get(id=_id)
        db.session.delete(user)
        db.session.commit()
