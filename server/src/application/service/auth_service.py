import datetime

import jwt

from bloxs.application.repository.user_repository import UserRepository

SECRET = "secret"


class AuthService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def login(self, email, password):
        user = self.user_repo.get_by_email(email)
        if user and user.check_password(password):
            payload = {
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
                "iat": datetime.datetime.utcnow(),
                "user": str(user.id),
            }
            return jwt.encode(payload, SECRET, algorithm="HS256")
        raise Exception("Invalid credentials")

    def validate_token(self, token):
        try:
            payload = jwt.decode(token, SECRET, algorithms=["HS256"])
            return payload["user"]
        except jwt.ExpiredSignatureError:
            raise Exception("Expired token")
        except jwt.InvalidTokenError:
            raise Exception("Invalid token")
