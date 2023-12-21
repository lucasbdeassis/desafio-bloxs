from functools import wraps

from flask import g, request

from bloxs.infra.DI.injector_factory import InjectorFactory


def requires_auth():
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get("Authorization")
            if not token:
                return {"error": "missing authorization header"}, 401
            with InjectorFactory().get_auth_service() as auth_service:
                g.user_id = auth_service.validate_token(token)
            return f(*args, **kwargs)

        return decorated

    return decorator
