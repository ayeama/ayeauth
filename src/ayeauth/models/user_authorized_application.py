from ayeauth import db
from ayeauth.models import BaseModel


class UserAuthorizedApplication(BaseModel):
    __tablename__ = "user_authorized_applications"

    user_id = db.Column(db.String(36), db.ForeignKey("users.id"))
    application_id = db.Column(db.String(36), db.ForeignKey("applications.id"))
