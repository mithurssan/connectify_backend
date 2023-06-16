from flask_jwt_extended import create_access_token


def generate_access_token(app, identity):
    with app.app_context():
        return create_access_token(identity)

#POST users test
def test_create_user(client, mock_user):
    res = client.post("/users/register", json=mock_user)
    assert res.status_code == 200

#POST duplicate users test
def test_create_duplicate_user(client, mock_user):
    res = client.post("/users/register", json=mock_user)
    assert res.json["error"] == "Username already exist"

#GET all users test
def test_get_all_users(client, mock_user):
    token = generate_access_token(client.application, mock_user["user_username"])

    headers = {"Authorization": f"Bearer {token}"}

    res = client.get("/users/", headers=headers)
    assert res.status_code == 200

    expected_user = {
        "user_username": "test",
    }
    response_json = res.get_json()

    assert any(expected_user.items() <= user.items() for user in response_json)

#POST user login test
def test_login_user(client, mock_user):
    res = client.post("/users/login", json=mock_user)
    assert res.status_code == 200


#GET business by id test
def test_get_user_by_id(client, mock_user):
    #login and get id
    res = client.post("/users/login", json=mock_user)
    assert res.status_code == 200
    user_id = res.json["user_id"] 

    res = client.get(f"/users/{user_id}")
    assert res.status_code == 200 

#PUT business test
def test_update_user(client, mock_user):
    #login and get id
    res = client.post("/users/login", json=mock_user)
    assert res.status_code == 200
    user_id = res.json["user_id"] 

    #update content
    updated_user = {
        "user_email": "test22@gmail.com",
        "user_username": "test",
        "user_password": "pass"
    }

    #sending update
    res = client.put(f"/users/update/{user_id}", json=updated_user)
    assert res.status_code == 200

    #making sure its updated
    res = client.get(f"/users/{user_id}")
   
    assert res.status_code == 200
    assert res.json["user_email"] == "test22@gmail.com"

# #DELETE business test
# def test_delete_user(client, mock_business):
#     #login and get id
#     res = client.post("/users/login", json=mock_user)
#     assert res.status_code == 200
#     business_id = res.json["username"] 

#     #delete user
#     res = client.delete(f"/users/delete/{user_username}")
#     assert res.status_code == 200

#     #making sure its deleted
#     res = client.get(f"/users/{user_username}")
#     assert res.status_code == 404
