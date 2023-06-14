from dotenv import load_dotenv
load_dotenv()
import pytest
from testing.postgresql import Postgresql
from application import app 
from sqlalchemy import create_engine
from os import environ

#setup postgres test database and test client
@pytest.fixture(scope="module")
def test_db():
    # environ["USE_MOCK_DB"] = "True"
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
        "business_id": "5af399184b2e4d33a0fb4f22f9ed5818",
        "user_id": "5743b701f72049b0ad39d84fcea6dbe9",
        "holiday_start_date": "1st of Jan",
        "holiday_end_date": "2nd of Feb",
        "holiday_status": "on holiday"
    }

