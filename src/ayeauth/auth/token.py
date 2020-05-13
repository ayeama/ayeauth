from datetime import datetime, timedelta

import jwt
from flask import current_app


def encode_jwt(user_id):
    now = datetime.utc_now()
    secret = current_app.config["JWT_SECRET_KEY"]
    algorithm = current_app.config["JWT_ALGORITHM"]

    expiration = now + timedelta(seconds=current_app.config["JWT_EXPIRATION"])
    not_before = now
    issuer = current_app.config["JWT_ISSUER"]
    audience = current_app.config["JWT_AUDIENCE"]
    issued_at = now

    payload = {
        "id": user_id,
        "exp": expiration,
        "nbf": not_before,
        "iss": issuer,
        "aud": audience,
        "iat": issued_at,
    }

    return jwt.encode(payload, secret, algorithums=list(algorithm))


def decode_jwt(token):
    secret = current_app.config["JWT_SECRET_KEY"]
    algorithm = current_app.config["JWT_ALGORITHM"]
    audience = current_app.config["JWT_AUDIENCE"]
    return jwt.decode(
        token, secret, audience=list(audience), algorithms=list(algorithm)
    )
