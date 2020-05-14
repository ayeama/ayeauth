from functools import wraps

from flask_principal import Permission, RoleNeed

from ayeauth import lm


def roles_required(*roles):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            permissions = [Permission(RoleNeed(role)) for role in roles]
            for p in permissions:
                if not p.can():
                    return lm.unauthorized()
            return fn(*args, **kwargs)

        return decorated_view

    return wrapper


def roles_accepted(*roles):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            permission = Permission(*[RoleNeed(role) for role in roles])
            if permission.can():
                return fn(*args, **kwargs)
            return lm.unauthorized()

        return decorated_view

    return wrapper
