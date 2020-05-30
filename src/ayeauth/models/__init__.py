import uuid
from datetime import datetime

from ayeauth import db


def _get_uuid():
    return str(uuid.uuid4())


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.String(36), nullable=False, primary_key=True, default=_get_uuid)
    created = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    updated = db.Column(
        db.DateTime(), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    deleted = db.Column(db.Boolean(), nullable=False, default=False)

    def __eq__(self, other):
        return str(self.id) == str(other.id)

    def __repr__(self):
        return str(self.id)
