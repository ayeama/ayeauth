from flask_login import current_user
from flask_principal import Identity, RoleNeed, UserNeed

from ayeauth.auth.token import decode_jwt
from ayeauth.models.user import User


def user_loader(user_id):
    return User.query.filter_by(id=user_id).first()


def request_loader(request):
    user = None
    auth_header = request.headers.get("Authorization")
    if auth_header is not None:
        auth_type, auth_token = auth_header.split(" ")

        if auth_type == "Bearer":
            payload = decode_jwt(auth_token)
            user = User.query.filter_by(id=payload["id"]).first()
        elif auth_type == "Basic":
            raise NotImplementedError()

    return user


def identity_loader():
    return Identity(current_user.id)


def on_identity_loaded(sender, identity):
    if hasattr(current_user, "id"):
        identity.provides.add(UserNeed(current_user.id))
    for role in getattr(current_user, "roles", []):
        identity.provides.add(RoleNeed(role.name))
    identity.user = current_user
