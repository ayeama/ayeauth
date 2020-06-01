import os


def _read_key(path):
    key = ""
    with open(path, "r") as f:
        key = f.read()
    return key


class Config:
    DEBUG = True
    SECRET_KEY = "thisisasecret"

    AUTHORIZATION_CODE_EXPIRY = 60 * 60

    JWT_ALGORITHM = "RS256"
    JWT_PRIVATE_KEY = _read_key(os.environ["JWT_PRIVATE_KEY"])
    JWT_PUBLIC_KEY = _read_key(os.environ["JWT_PUBLIC_KEY"])
    JWT_EXPIRATION = 60 * 60 * 24
    JWT_ISSUER = "ayeauth"
    JWT_AUDIENCE = "ayeama:ayeauth"

    SQLALCHEMY_DATABASE_URI = "sqlite:///../../env/ayeauth.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
