from flask_login import UserMixin as BaseUserMixin
from flask_security.utils import hash_password

from ayeauth import db
from ayeauth.models import BaseDatastore, BaseModel
from ayeauth.models.role import RoleDatastore


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
        return self.id

    def __str__(self):
        return f"{self.__class__.__name__}({self.username})"


class UserDatastore(BaseDatastore):
    def get(self, id, many=False):
        if many:
            return User.query.all()
        return User.query.filter_by(id=id).first()

    def post(self, username, password):
        password = hash_password(password)
        user = User(username=username, password=password)
        db.session.add(user)
        self.commit()
        return user

    def put(self, id, username, password):
        user = self.get(id=id)
        if username is not None:
            user.username = username
        if password is not None:
            user.password = hash_password(password)
        self.commit()
        return user

    def delete(self, username):
        user = self.get(username=username)
        db.session.delete(user)
        self.commit()
        return user

    def add_role(self, user_id, role_id):
        user = self.get(user_id)
        role = RoleDatastore().get(role_id)
        user.roles.append(role)
        self.commit()
        return user

    def get_roles(self, user_id):
        user = self.get(user_id)
        roles = user.roles
        return roles

    def delete_role(self, user_id, role_id):
        user = self.get(user_id)
        role = RoleDatastore().get(role_id)
        user.roles.remove(role)
        self.commit()
        return user
