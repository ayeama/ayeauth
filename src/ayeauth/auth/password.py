from passlib.hash import bcrypt


def hash_password(password):
    return bcrypt.hash(password)


def verify_password(password, hashed_password):
    return bcrypt.verify(password, hashed_password)
