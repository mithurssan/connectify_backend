import json
import requests
from os import environ
from application.controllers import BusinessController
from application.models import Business
from flask import Blueprint, request, jsonify, session
from application import bcrypt
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import (
    create_access_token,
    unset_jwt_cookies,
    get_jwt_identity,
    get_jwt,
    jwt_required,
)

business = Blueprint("business", __name__)


@business.route("/")
@jwt_required()
def get_businesses():
    businesses = BusinessController.get_all_businesses()
    business_list = []
    for business in businesses:
        business_list.append(format_business(business))
    return jsonify(business_list), 200


def format_business(business):
    return {
        "id": business.business_id,
        "business_name": business.business_name,
        "password": business.business_password,
    }


@business.route("/<business_id>", methods=["GET"])
def get_business_by_id(business_id):
    business = BusinessController.get_one_by_business_id(business_id)
    if business:
        return jsonify(format_business(business))
    else:
        return jsonify({"message": "Business not found"})


@business.route("/update/<int:business_id>", methods=["PUT"])
def update_business(business_id):
    data = request.json
    business_name = data.get("business_name")
    password = data.get("password")
    BusinessController.update_user(business_id, business_name, password)
    return jsonify({"message": "Business updated successfully"})


@business.route("/delete/<int:business_id>", methods=["DELETE"])
def delete_business(business_id):
    BusinessController.delete_user(business_id)
    return jsonify({"message": "Business deleted successfully"})


@business.route("/register", methods=["POST"])
def register_business():
    data = request.json
    # print(data)
    business_name = data.get("business_name")
    email = data.get("business_email")
    number = data.get("business_number")
    password = data.get("business_password")

    business_exist = (
        Business.query.filter_by(business_name=business_name).first() is not None
    )

    if business_exist:
        return jsonify({"error": "Business already exist"})

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    new_business = Business(
        business_name=business_name,
        business_password=hashed_password,
        business_email=email,
        business_number=number,
    )

    session["user_id"] = new_business.business_id

    BusinessController.register_business(business_name, hashed_password, email, number)

    # response = requests.post(
    #     "https://api.chatengine.io/users/",
    #     data={
    #         "username": request.get_json()["business_username"],
    #         "secret": request.get_json()["business_password"],
    #         "email": request.get_json()["business_email"],
    #     },
    #     headers={"Private-Key": "7f306ed8-bf91-4841-b5e1-f9bf00e39ddf"},
    # )

    return jsonify(
        {
            "business_name": business_name,
            "password": hashed_password,
            "number": number,
            "email": email,
        }
    )
    # response.json()


@business.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original response
        return response


@business.route("/login", methods=["POST"])
def login_business():
    data = request.json
    business_name = data.get("business_name")
    password = data.get("business_password")

    business = Business.query.filter_by(business_name=business_name).first()

    if business is None:
        return jsonify({"error": "Unauthorized access"}), 401

    if not bcrypt.check_password_hash(business.business_password, password):
        return jsonify({"error": "Unauthorized"}), 401
    access_token = create_access_token(identity=business_name)
    session["business_id"] = business.business_id

    # response = requests.get(
    #     "https://api.chatengine.io/users/me/",
    #     headers={
    #         "Project-ID": "7f8e7fee-521a-4f50-8d9a-9028fc529c34",
    #         "User-Name": request.get_json()["business_name"],
    #         "User-Secret": request.get_json()["business_password"],
    #     },
    # )

    return jsonify({"business_name": business_name, "token": access_token})
    # response.json()
