def test_login(client):
    response = client.post(
        "/auth/login",
        json={
            "email": "john.doe@example.com",
            "password": "password",
        },
    )
    assert response.status_code == 200
    assert response.json["token"] is not None


def test_validate(client):
    response = client.post(
        "/auth/login",
        json={
            "email": "john.doe@example.com",
            "password": "password",
        },
    )
    token = response.json["token"]
    response = client.post(
        "/auth/validate",
        json={
            "token": token,
        },
    )
    assert response.status_code == 200
    assert response.json["user_id"] is not None
