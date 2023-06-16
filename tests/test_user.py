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

#POST wrong username login test
def test_user_login_wrong_username(client, mock_wrong_user_username):
    res = client.post("/users/login", json=mock_wrong_user_username)
    assert res.status_code == 401

#POST wrong password login test
def test_user_login_wrong_password(client, mock_wrong_user_password):
    res = client.post("/users/login", json=mock_wrong_user_password)
    assert res.status_code == 401

#GET user by id test
def test_get_user_by_id(client, mock_user):
    #login and get id
    res = client.post("/users/login", json=mock_user)
    assert res.status_code == 200
    user_id = res.json["user_id"] 

    res = client.get(f"/users/{user_id}")
    assert res.status_code == 200 

#PUT user_email test
def test_update_email_user(client, mock_user):
    #login and get id
    res = client.post("/users/login", json=mock_user)
    assert res.status_code == 200
    user_id = res.json["user_id"] 

    #update content
    updated_user = {
        "user_email": "test22@gmail.com"
    }

    #sending update
    res = client.patch(f"/users/update/{user_id}", json=updated_user)
    assert res.status_code == 200

    #making sure its updated
    res = client.get(f"/users/{user_id}")
   
    assert res.status_code == 200
    assert res.json["user_email"] == "test22@gmail.com"

#PUT user_username test
def test_update_username_user(client, mock_user):
    #login and get id
    res = client.post("/users/login", json=mock_user)
    assert res.status_code == 200
    user_id = res.json["user_id"] 

    #update content
    updated_user = {
        "user_username": "test22"
    }

    #sending update
    res = client.patch(f"/users/update/{user_id}", json=updated_user)
    assert res.status_code == 200

    #making sure its updated
    res = client.get(f"/users/{user_id}")
   
    assert res.status_code == 200
    assert res.json["user_username"] == "test22"

#PUT user_password test
def test_update_password_user(client):
    updated_user = {
        "user_username": "test22",
        "user_password": "pass"
    }
    #login and get id
    res = client.post("/users/login", json=updated_user)
    assert res.status_code == 200
    user_id = res.json["user_id"]

    #update content
    updated_user = {
        "user_password": "pass2"
    }

    #sending update
    res = client.patch(f"/users/update/{user_id}", json=updated_user)
    assert res.status_code == 200

    #making sure its updated
    res = client.get(f"/users/{user_id}")
    assert res.status_code == 200
    assert res.json["user_password"] == "pass2"

#DELETE user test
def test_delete_user(client, mock_user):
    #create new user as previous has been updated
    res = client.post("/users/register", json=mock_user)
    assert res.status_code == 200

    #login and get id
    res = client.post("/users/login", json=mock_user)
    assert res.status_code == 200
    user_id = res.json["user_id"] 
    print(user_id)
    #delete user
    res = client.delete(f"/users/delete/{user_id}")
    assert res.status_code == 200

    #making sure its deleted
    res = client.get(f"/users/{user_id}")
    assert res.status_code == 404

