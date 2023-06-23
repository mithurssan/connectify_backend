import base64
from flask import Flask
from unittest.mock import patch

from application.routes.CompaniesHouseProxy import proxy


def test_get_company_summary():
    app = Flask(__name__)
    app.register_blueprint(proxy)

    with app.test_client() as client:
        # Patching the requests.get function to mock the API response
        with patch(proxy.requests.get) as mock_get:
            # Mock the API response
            mock_response = {
                "name": "Test Company",
                "registration_number": "123456789",
                # Add other fields as per the expected response
            }
            mock_get.return_value.json.return_value = mock_response

            # Perform a GET request to the endpoint
            response = client.get("/company/123456789")

            # Assert that the request was successful (status code 200)
            assert response.status_code == 200

            # Assert that the response contains the expected data
            assert response.json == mock_response

            # Assert that the API request was made with the correct headers
            mock_get.assert_called_once_with(
                "https://api.company-information.service.gov.uk/company/123456789",
                headers={
                    "Authorization": "...",  # Replace with the expected authorization header
                    "Content-Type": "application/json",
                },
            )
