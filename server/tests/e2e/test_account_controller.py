def test_get_account(client, auth_token):
    response = client.get(
        "/accounts/b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12",
        headers={"Authorization": auth_token},
    )
    assert response.status_code == 200
    assert response.json["id"] == "b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12"
    assert response.json["user_id"] == "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    assert response.json["max_daily_withdraw"] == 10000
    assert response.json["is_active"] is True
    assert response.json["type"] == 1


def test_create_account(client, auth_token):
    response = client.post(
        "/accounts",
        json={
            "user_id": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11",
            "balance": 1000,
            "name": "Test",
            "max_daily_withdraw": 10000,
            "is_active": True,
            "type": 1,
        },
        headers={"Authorization": auth_token},
    )
    assert response.status_code == 201
    assert response.json["id"] is not None
    assert response.json["user_id"] == "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    assert response.json["balance"] == 1000
    assert response.json["max_daily_withdraw"] == 10000
    assert response.json["is_active"] is True
    assert response.json["type"] == 1


def test_make_deposit(client, auth_token):
    response = client.post(
        "/accounts/b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12/deposit",
        json={"value": 100},
        headers={"Authorization": auth_token},
    )
    assert response.status_code == 200
    assert response.json["id"] == "b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12"


def test_make_withdraw(client, auth_token):
    response = client.post(
        "/accounts/b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12/withdraw",
        json={"value": 100},
        headers={"Authorization": auth_token},
    )
    assert response.status_code == 200
    assert response.json["id"] == "b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12"


def test_block_account(client, auth_token):
    response = client.post(
        "/accounts/b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12/block",
        headers={"Authorization": auth_token},
    )
    assert response.status_code == 200
    assert response.json["id"] == "b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12"
    assert response.json["is_active"] is False


def test_unblock_account(client, auth_token):
    response = client.post(
        "/accounts/b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12/unblock",
        headers={"Authorization": auth_token},
    )
    assert response.status_code == 200
    assert response.json["id"] == "b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12"
    assert response.json["is_active"] is True


def test_get_account_transactions(client, auth_token):
    response = client.get(
        "/accounts/b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12/transactions",
        headers={"Authorization": auth_token},
    )
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_list_accounts(client, auth_token):
    response = client.get("/accounts", headers={"Authorization": auth_token})
    assert response.status_code == 200
    assert isinstance(response.json, list)
