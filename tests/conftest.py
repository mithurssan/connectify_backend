import pytest
from os import environ

#set env value to use mock sqlite db for testing
environ["USE_MOCK_DB"] = "True"
from application import app 
app.config["SECRET_KEY"] = "test_secret_key"

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

@pytest.fixture
def mock_journal_entry():
    return {
        "user_id": "test_user",
        "entry_date": "14-06-2023",
        "entry_title": "First Entry",
        "entry_content": "hello there, this is my first journal entry!"
    }

@pytest.fixture
def mock_rota():
    return {
        "business_id":"test_business",
        "rota_start_date": "15-06-2023",
        "rota_end_date": "20-06-2023",
        "rota_content": "Assigned to user: test"
    }

@pytest.fixture
def mock_business():
    return {
        "business_email": "test@gmail.com",
        "business_name": "testBusiness",
        "business_number": 1,
        "business_password": "pass"
    }
