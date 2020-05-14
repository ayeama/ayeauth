from enum import Enum

from ayeauth import db
from ayeauth.models import BaseModel


class ScopeAccess(Enum):
    NO_ACCESS = "no access"
    READ_ONLY = "read only"
    READ_WRITE = "read and write"


class Scope(BaseModel):
    __tablename__ = "scopes"

    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return str(self.name)
