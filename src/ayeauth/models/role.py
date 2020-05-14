from ayeauth import db
from ayeauth.models import BaseModel


class RoleMixin:
    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __hash__(self):
        pass


class Role(BaseModel, RoleMixin):
    __tablename__ = "roles"

    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255), unique=False)

    def __repr__(self):
        return str(self.id)

    def __str__(self):
        return str(self.name)
