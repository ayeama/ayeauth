from ayeauth import db
from ayeauth.models import BaseModel, _get_uuid


class Application(BaseModel):
    __tablename__ = "applications"

    name = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String())
    redirect_uri = db.Column(db.String(), nullable=False)
    client_id = db.Column(db.String(36), nullable=False, default=_get_uuid)

    scopes = db.relationship("ApplicationScope", back_populates="application")
    owner_id = db.Column(db.String(36), db.ForeignKey("users.id"))

    def __init__(self, name, description, redirect_uri, owner):
        super(Application, self).__init__()

        self.name = name
        self.description = description
        self.redirect_uri = redirect_uri
        self.owner = owner

    def __str__(self):
        return str(self.name)
