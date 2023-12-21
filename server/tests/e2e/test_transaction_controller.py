def test_list_transactions(client, auth_token):
    response = client.get("/transactions", headers={"Authorization": auth_token})
    assert response.status_code == 200
    assert isinstance(response.json, list)
