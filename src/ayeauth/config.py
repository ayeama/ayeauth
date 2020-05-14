class Config:
    DEBUG = True
    SECRET_KEY = "thisisasecret"

    JWT_ALGORITHM = "HS256"
    JWT_SECRET_KEY = "thisisasecret"
    JWT_EXPIRATION = 60 * 60 * 24
    JWT_ISSUER = "ayeauth"
    JWT_AUDIENCE = "ayeama:ayeauth"

    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/ayeauth.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
