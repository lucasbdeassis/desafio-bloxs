from flask import blueprints, request

from bloxs.infra.DI.injector_factory import InjectorFactory

auth_controller = blueprints.Blueprint("auth_controller", __name__)

di_factory = InjectorFactory()


@auth_controller.route("/auth/login", methods=["POST"])
def login():
    with di_factory.get_auth_service() as auth_service:
        token = auth_service.login(request.json["email"], request.json["password"])
        return {"token": token}


@auth_controller.route("/auth/validate", methods=["POST"])
def validate():
    with di_factory.get_auth_service() as auth_service:
        user_id = auth_service.validate_token(request.json["token"])
        return {"user_id": user_id}
