from enum import Enum

from ayeauth import db
from ayeauth.models import BaseModel


class ScopeAccess(Enum):
    NO_ACCESS = "No access"
    READ_ONLY = "Read only"
    READ_AND_WRITE = "Read and write"


class Scope(BaseModel):
    __tablename__ = "scopes"

    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255))

    applications = db.relationship("ApplicationScope", back_populates="scope")

    def __init__(self, name, description):
        super(Scope, self).__init__()

        self.name = name
        self.description = description

    def __str__(self):
        return str(self.name)
