from ayeauth import db
from ayeauth.models import BaseModel, _get_uuid


class Application(BaseModel):
    __tablename__ = "applications"

    name = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String())
    callback_url = db.Column(db.String(), nullable=False)
    client_id = db.Column(db.String(36), nullable=False, default=_get_uuid)

    def __init__(self, name, description, callback_url):
        super(Application, self).__init__()

        self.name = name
        self.description = description
        self.callback_url = callback_url

    def __str__(self):
        return str(self.name)
