from ayeauth import db
from ayeauth.models import BaseModel, _get_uuid


class AuthorizationCode(BaseModel):
    __tablename__ = "authorization_codes"

    code = db.Column(db.String(36), nullable=False, default=_get_uuid)
    expiry = db.Column(db.DateTime(), nullable=False)
    state = db.Column(db.String(36), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"))
    application_id = db.Column(db.String(36), db.ForeignKey("applications.id"))

    def __init__(self, expiry, state, user_id, application_id):
        self.expiry = expiry
        self.state = state
        self.user_id = user_id
        self.application_id = application_id
