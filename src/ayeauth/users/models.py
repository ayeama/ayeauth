import uuid

from flask_security import RoleMixin, UserMixin

from ayeauth import db


class UserRole(db.Model):
    __tablename__ = 'users_roles'

    id = db.Column(db.String(36), primary_key=True, default=uuid.uuid4)
    db.Column('user_id', db.String(36), db.ForeignKey('user.id'))
    db.Column('role_id', db.String(36), db.ForeignKey('role.id'))


class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'

    id = db.Column(db.String(36), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship(
        'Role',
        secondary='users_roles',
        backref=db.backref('users', lazy='dynamic')
    )
