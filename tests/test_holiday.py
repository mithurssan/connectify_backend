#POST holiday booking test
def test_create_booking(client, mock_booking):
    res = client.post("/bookings/book", json=mock_booking)
    assert res.status_code == 200

#GET all holiday bookings test
def test_get_all_bookings(client):
    res = client.get("/bookings/")
    assert res.status_code == 200

    expected_booking = [
        {
            "business_id": "test_business_id",
            "holiday_end_date": "2nd of Feb",
            "holiday_id": 1,
            "holiday_start_date": "1st of Jan",
            "holiday_status": "on holiday",
            "user_id": "test_user_id",
        }
    ]
    assert res.json == expected_booking

#GET holiday booking by id test
def test_get_booking_by_id(client):
    res = client.get("/bookings/1")
    assert res.status_code == 200 

#PUT holiday booking test
def test_update_booking(client, mock_booking):
    #update status
    updated_booking = mock_booking.copy()
    updated_booking["holiday_status"] = "back from holiday"

    #sending update
    res = client.put("/bookings/update/1", json=updated_booking)
    assert res.status_code == 200

    #making sure its updated
    res = client.get("/bookings/1")
    assert res.status_code == 200
    assert res.json["holiday_status"] == "back from holiday"

#DELETE holiday booking
def test_delete_holiday(client, mock_booking):
    #get booking
    res = client.get("/bookings/1", json=mock_booking)
    assert res.status_code == 200

    #delete booking
    res = client.delete("/bookings/delete/1")
    assert res.status_code == 200

    #making sure its deleted
    res = client.get("/bookings/1")
    assert res.status_code == 404
