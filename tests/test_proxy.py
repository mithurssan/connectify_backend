import base64
from unittest.mock import patch

import pytest
import requests
from flask import Flask

from application.routes.CompaniesHouseProxy import proxy


@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(proxy)

    with app.test_client() as client:
        yield client


def test_get_company_summary_success(client):
    company_number = "12345678"
    api_key = "dummy_api_key"
    encoded_api_key = base64.b64encode(api_key.encode("utf-8")).decode("utf-8")
    authorization_header = f"Basic {encoded_api_key}"
    expected_url = (
        f"https://api.company-information.service.gov.uk/company/{company_number}"
    )
    expected_headers = {
        "Authorization": authorization_header,
        "Content-Type": "application/json",
    }
    expected_data = {"name": "Company ABC", "address": "123 Main St"}

    with patch.object(requests, "get") as mock_get:
        response_mock = mock_get.return_value
        response_mock.json.return_value = expected_data
        response_mock.status_code = 200

        response = client.get(f"/company/{company_number}")

        mock_get.assert_called_once_with(expected_url, headers=expected_headers)
        assert response.status_code == 200
        assert response.get_json() == expected_data


def test_get_company_summary_request_error(client):
    company_number = "12345678"
    api_key = "dummy_api_key"
    encoded_api_key = base64.b64encode(api_key.encode("utf-8")).decode("utf-8")
    authorization_header = f"Basic {encoded_api_key}"
    expected_url = (
        f"https://api.company-information.service.gov.uk/company/{company_number}"
    )
    expected_headers = {
        "Authorization": authorization_header,
        "Content-Type": "application/json",
    }
    expected_error = "Request error"

    with patch.object(requests, "get") as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException(expected_error)

        response = client.get(f"/company/{company_number}")

        mock_get.assert_called_once_with(expected_url, headers=expected_headers)
        assert response.status_code == 500
        assert response.get_json() == {"error": str(expected_error)}


def test_get_company_summary_invalid_api_key(client, monkeypatch):
    company_number = "12345678"
    api_key = None
    expected_error = "Invalid API key"

    monkeypatch.setenv("CH_API_KEY", api_key)

    response = client.get(f"/company/{company_number}")

    assert response.status_code == 500
    assert response.get_json() == {"error": expected_error}
