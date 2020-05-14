from ayeauth import db, _get_uuid
from ayeauth.models import BaseModel


class Application(BaseModel):
    __tablename__ = "applications"

    name = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String())
    callback_url = db.Column(db.String(), nullable=False)
    client_id = db.Column(db.String(36), nullable=False, default=_get_uuid)
    scopes = db.relationship("Scope", secondary="application_scopes", backref=db.backref("applications", lazy="dynamic"))

    def __init__(self, name, description, callback_url):
        super(Application, self).__init__()

        self.name = name
        self.description = description
        self.callback_url = callback_url

    def __str__(self):
        return str(self.name)
