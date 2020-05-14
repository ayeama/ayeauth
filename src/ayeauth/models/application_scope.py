from ayeauth import db
from ayeauth.models import BaseModel
from ayeauth.models.scope import ScopeAccess


class ApplicationScope(BaseModel):
    __tablename__ = "application_scopes"

    application_id = db.Column(db.String(36), db.ForeignKey("applications.id"))
    scope_id = db.Column(db.String(36), db.ForeignKey("scopes.id"))
    access = db.Column(db.Enum(ScopeAccess), nullable=False, default=ScopeAccess.NO_ACCESS)
