from flask_jwt_extended import create_access_token

def generate_access_token(app, identity):
    with app.app_context():
        return create_access_token(identity)

#POST business test
def test_create_business(client, mock_business):
    res = client.post("/businesses/register", json=mock_business)
    assert res.status_code == 200

#POST duplicate business test
def test_create_duplicate_business(client, mock_business):
    res = client.post("/businesses/register", json=mock_business)
    assert res.json["error"] == "Business already exists"

#GET all businesses test
def test_get_all_businesses(client, mock_business):
    token = generate_access_token(client.application, mock_business["business_name"])

    headers = {"Authorization": f"Bearer {token}"}

    res = client.get("/businesses/", headers=headers)
    assert res.status_code == 200

    expected_business = {
        "business_name": "testBusiness",
    }
    response_json = res.get_json()

    assert any(expected_business.items() <= business.items() for business in response_json)

#POST business login test
def test_login_business(client, mock_business):
    res = client.post("/businesses/login", json=mock_business)
    assert res.status_code == 200

#POST wrong username login test
def test_business_login_wrong_username(client, mock_wrong_business_username):
    res = client.post("/businesses/login", json=mock_wrong_business_username)
    assert res.status_code == 401

#POST wrong password login test
def test_business_login_wrong_password(client, mock_wrong_business_password):
    res = client.post("/businesses/login", json=mock_wrong_business_password)
    assert res.status_code == 401

#GET business by id test
def test_get_business_by_id(client, mock_business):
    #login and get id
    res = client.post("/businesses/login", json=mock_business)
    assert res.status_code == 200
    business_id = res.json["business_id"] 

    res = client.get(f"/businesses/{business_id}")
    assert res.status_code == 200 

#PUT business test
def test_update_business(client, mock_business):
    #login and get id
    res = client.post("/businesses/login", json=mock_business)
    assert res.status_code == 200
    business_id = res.json["business_id"] 

    #update content
    updated_business = {
        "business_email": "business2@gmail.com",
        "business_name": "testBusiness",
        "business_number": 1,
        "business_password": "pass"
    }

    #sending update
    res = client.put(f"/businesses/update/{business_id}", json=updated_business)
    assert res.status_code == 200

    #making sure its updated
    res = client.get(f"/businesses/{business_id}")
   
    assert res.status_code == 200
    assert res.json["business_email"] == "business2@gmail.com"

#DELETE business test
def test_delete_business(client, mock_business):
    #login and get id
    res = client.post("/businesses/login", json=mock_business)
    assert res.status_code == 200
    business_id = res.json["business_id"] 

    #delete business
    res = client.delete(f"/businesses/delete/{business_id}")
    assert res.status_code == 200

    #making sure its deleted
    res = client.get(f"/businesses/{business_id}")
    assert res.status_code == 404
