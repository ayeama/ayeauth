from ayeauth import db
from ayeauth.models import BaseModel


class UserRole(BaseModel):
    __tablename__ = "user_roles"

    user_id = db.Column(db.String(36), db.ForeignKey("users.id"))
    role_id = db.Column(db.String(36), db.ForeignKey("roles.id"))
