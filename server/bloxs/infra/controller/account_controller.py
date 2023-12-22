from flask import blueprints, g, request

from bloxs.infra.controller.auth import requires_auth
from bloxs.infra.DI.injector_factory import InjectorFactory

account_controller = blueprints.Blueprint("account_controller", __name__)


@account_controller.route("/accounts/<account_id>", methods=["GET"])
@requires_auth()
def get_account(account_id):
    with InjectorFactory().get_account_service() as account_service:
        account = account_service.get(g.user_id, account_id)
        return account.model_dump(), 200


@account_controller.route("/accounts", methods=["GET"])
@requires_auth()
def get_accounts():
    with InjectorFactory().get_account_service() as account_service:
        accounts = account_service.list_accounts_by_user(g.user_id)
        return [account.model_dump() for account in accounts], 200


@account_controller.route("/accounts", methods=["POST"])
@requires_auth()
def create_account():
    with InjectorFactory().get_account_service() as account_service:
        input = {
            "user_id": g.user_id,
            "name": request.json["name"],
            "balance": request.json["balance"],
            "max_daily_withdraw": request.json["max_daily_withdraw"],
        }
        account = account_service.create(input)
        return account.model_dump(), 201


@account_controller.route("/accounts/<account_id>/deposit", methods=["POST"])
@requires_auth()
def make_deposit(account_id):
    with InjectorFactory().get_account_service() as account_service:
        account = account_service.make_deposit(
            g.user_id, account_id, request.json["value"]
        )
        return account.model_dump(), 200


@account_controller.route("/accounts/<account_id>/withdraw", methods=["POST"])
@requires_auth()
def make_withdraw(account_id):
    with InjectorFactory().get_account_service() as account_service:
        account = account_service.make_withdraw(
            g.user_id, account_id, request.json["value"]
        )
        return account.model_dump(), 200


@account_controller.route("/accounts/<account_id>/block", methods=["POST"])
@requires_auth()
def block_account(account_id):
    with InjectorFactory().get_account_service() as account_service:
        account = account_service.block_account(g.user_id, account_id)
        return account.model_dump(), 200


@account_controller.route("/accounts/<account_id>/unblock", methods=["POST"])
@requires_auth()
def unblock_account(account_id):
    with InjectorFactory().get_account_service() as account_service:
        account = account_service.unblock_account(g.user_id, account_id)
        return account.model_dump(), 200


@account_controller.route("/accounts/<account_id>/transactions", methods=["GET"])
@requires_auth()
def get_account_transactions(account_id):
    with InjectorFactory().get_transaction_service() as transaction_service:
        transactions = transaction_service.list_transaction_by_account(account_id)
        return [transaction.model_dump() for transaction in transactions], 200
