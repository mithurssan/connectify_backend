#GET all holiday bookings test
def test_get_bookings(client):
    res = client.get('/bookings/')
    assert res.status_code == 200 

#POST holiday booking test
def test_create_holiday(client, mock_booking):
    res = client.post('/bookings/book', json=mock_booking)
    assert res.status_code == 200


#Temp User creation test to prevent violation of foreign key constraint 
# def test_register_user(client, mock_user):
#     res = client.post("/users/register", json=mock_user)
#     assert res.status_code == 200


