from os import environ
import base64
import requests
from flask import jsonify, Blueprint

# from application import app

proxy = Blueprint("proxy", __name__)


@proxy.route("/company/<company_number>")
def get_company_summary(company_number):
    api_key = environ.get("CH_API_KEY")
    encoded_api_key = base64.b64encode(api_key.encode("utf-8")).decode("utf-8")
    authorization_header = f"Basic {encoded_api_key}"
    print(authorization_header)

    url = f"https://api.company-information.service.gov.uk/company/{company_number}"
    headers = {
        "Authorization": authorization_header,
        "Content-Type": "application/json",
    }

    try:
        res = requests.get(url, headers=headers)
        data = res.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
