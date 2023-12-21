from flask import blueprints, g

from bloxs.infra.controller.auth import requires_auth
from bloxs.infra.DI.injector_factory import InjectorFactory

transaction_controller = blueprints.Blueprint("transaction_controller", __name__)

di_factory = InjectorFactory()


@transaction_controller.route("/transactions", methods=["GET"])
@requires_auth()
def get_transactions():
    with InjectorFactory().get_transaction_service() as transaction_service:
        transactions = transaction_service.list_transactions_by_user(g.user_id)
        return [transaction.model_dump() for transaction in transactions], 200
