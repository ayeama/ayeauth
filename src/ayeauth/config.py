class Config:
    DEBUG = True
    SECRET_KEY = "thisisasecret"

    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/ayeauth.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECURITY_PASSWORD_SALT = "changeme"
    SECURITY_TOKEN_MAX_AGE = 60 * 60 * 24
    SECURITY_REGISTERABLE = True
    SECURITY_TRACKABLE = True

    SECURITY_USER_IDENTITY_ATTRIBUTES = ["username"]
