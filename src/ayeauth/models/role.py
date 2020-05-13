from ayeauth import db
from ayeauth.models import BaseDatastore, BaseModel


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
        return self.id

    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"


class RoleDatastore(BaseDatastore):
    def get(self, id, many=False):
        if many:
            return Role.query.all()
        return Role.query.filter_by(id=id).first()

    def post(self, name, description):
        role = Role(name=name, description=description)
        db.session.add(role)
        self.commit()
        return role

    def put(self, id, name, description):
        role = self.get(id=id)
        if name is not None:
            role.name = name
        if description is not None:
            role.description = description
        self.commit()
        return role

    def delete(self, id):
        role = self.get(id=id)
        db.session.delete(role)
        self.commit()
        return role
