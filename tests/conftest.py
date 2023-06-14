import pytest
from os import environ

#set env value to use mock sqlite db for testing
environ["USE_MOCK_DB"] = "True"
from application import app 

#use app as test_client
@pytest.fixture()
def client():
    with app.test_client() as test_client:
        yield test_client

#mock data
@pytest.fixture
def mock_booking():
    return {
        "business_id": "test_business_id",
        "user_id": "test_user_id",
        "holiday_start_date": "1st of Jan",
        "holiday_end_date": "2nd of Feb",
        "holiday_status": "on holiday"
    }

@pytest.fixture
def mock_user():
    return {
        "user_email": "test@gmail.com",
        "user_username": "test",
        "user_password": "pass"
    }
