from datetime import datetime, timedelta

import jwt
from flask import current_app


def encode_jwt(user_id, audience):
    now = datetime.utcnow()
    secret = current_app.config["JWT_PRIVATE_KEY"]
    algorithm = current_app.config["JWT_ALGORITHM"]

    expiration = now + timedelta(seconds=current_app.config["JWT_EXPIRATION"])
    not_before = now
    issuer = current_app.config["JWT_ISSUER"]
    issued_at = now

    payload = {
        "id": user_id,
        "exp": expiration,
        "nbf": not_before,
        "iss": issuer,
        "aud": audience,
        "iat": issued_at,
    }

    return jwt.encode(payload, secret, algorithm=algorithm)


def decode_jwt(token, audience):
    secret = current_app.config["JWT_PUBLIC_KEY"]
    algorithm = current_app.config["JWT_ALGORITHM"]
    return jwt.decode(token, secret, audience=audience, algorithms=algorithm)
