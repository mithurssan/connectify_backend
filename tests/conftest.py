import pytest
from testing.postgresql import Postgresql
from application import app 
from sqlalchemy import create_engine

#setup postgres test database and test client
@pytest.fixture(scope="module")
def test_db():
    with Postgresql() as postgresql:
        engine = create_engine(postgresql.url())
        yield engine

@pytest.fixture()
def client():
    with app.test_client() as test_client:
        yield test_client

#mock data
@pytest.fixture
def mock_booking():
    return {
        "business_id": 1,
        "user_id": 1,
        "holiday_start_date": "1st of Jan",
        "holiday_end_date": "2nd of Feb",
        "holiday_status": "on holiday"
    }


# Temp User mock data to prevent violation of foreign key constraint 
# @pytest.fixture
# def mock_user():
#     return {
#         "user_username": "test",
#         "user_password": "pass"
#     }

