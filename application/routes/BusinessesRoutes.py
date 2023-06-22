import json
import requests
from os import environ
from application.controllers import BusinessController
from application.models import Business
from flask import Blueprint, request, jsonify, session
from application import bcrypt, db
from datetime import datetime, timedelta, timezone
from application import mail
from uuid import uuid4
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    get_jwt,
    jwt_required,
)

business = Blueprint("business", __name__)


@business.route("/")
def get_businesses():
    businesses = BusinessController.get_all_businesses()
    business_list = []
    for business in businesses:
        business_list.append(format_business(business))
    return jsonify(business_list), 200


def format_business(business):
    return {
        "business_id": business.business_id,
        "business_email": business.business_email,
        "business_name": business.business_name,
        "business_password": business.business_password,
        "business_verify_token": business.business_verify_token,
        "business_verified": business.business_verified,
    }


@business.route("/<string:business_id>", methods=["GET"])
def get_business_by_id(business_id):
    business = BusinessController.get_one_by_business_id(business_id)
    if business:
        return jsonify(format_business(business))
    else:
        return jsonify({"message": "Business not found"}), 404


@business.route("/update/<string:business_id>", methods=["PUT"])
def update_business(business_id):
    data = request.json
    business_email = data["business_email"]
    business_email = data["business_email"]
    business_name = data["business_name"]
    business_password = data["business_password"]
    BusinessController.update_business(
        business_id, business_email, business_name, business_password
    )
    return jsonify({"message": "Business updated successfully"})


@business.route("/delete/<string:business_id>", methods=["DELETE"])
def delete_business(business_id):
    BusinessController.delete_business(business_id)
    return jsonify({"message": "Business deleted successfully"})


@business.route("/register", methods=["POST"])
def register_business():
    data = request.json

    business_email = data.get("business_email")
    business_name = data.get("business_name")
    business_number = data.get("business_number")
    business_password = data.get("business_password")
    verify_token = uuid4().hex
    verified = False

    if not business_name or not business_password:
        return jsonify({"error": "Enter business name and password"})

    if not business_email:
        return jsonify({"error": "Enter business email address"})

    business_exist = (
        Business.query.filter_by(business_name=business_name).first() is not None
    )

    if business_exist:
        return jsonify({"error": "Business already exists"})

    hashed_password = bcrypt.generate_password_hash(business_password).decode("utf-8")
    new_business = Business(
        business_name=business_name,
        business_password=hashed_password,
        business_email=business_email,
        business_number=business_number,
        business_verify_token=verify_token,
        business_verified=verified,
    )

    session["user_id"] = new_business.business_id

    BusinessController.register_business(
        business_name,
        hashed_password,
        business_email,
        business_number,
        verify_token,
        verified,
    )

    send_verification_email(business_email, verify_token)

    response = requests.post(
        "https://api.chatengine.io/users/",
        data={
            "username": request.get_json()["business_name"],
            "secret": hashed_password,
            "email": request.get_json()["business_email"],
        },
        headers={"Private-Key": "7f306ed8-bf91-4841-b5e1-f9bf00e39ddf"},
    )

    return (
        jsonify(
            {
                "business_name": business_name,
                "password": hashed_password,
                "number": business_number,
                "email": business_email,
                "verify_token": verify_token,
                "verified": verified,
            }
        ),
        response.json(),
    )


def send_verification_email(email, verify_token):
    verification_link = f"https://connectifysite.netlify.app/businesses/verify/{verify_token}"

    mail.send_message(
        "BUSINESS - Verify your email",
        sender=environ.get("EMAIL"),
        recipients=[email],
        html=f"<h1>Connectify</h1> \n <h4>Please, use the link below to verify your email:</h4> \n <p><b>{verification_link}</b></p>",
    )


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
    access_token = create_access_token(
        identity=business_name, additional_claims={"business_id": business.business_id}
    )

    session["business_id"] = business.business_id

    response = requests.get(
        "https://api.chatengine.io/users/me/",
        headers={
            "Project-ID": environ.get("CHAT_ENGINE_PROJECT_ID"),
            "User-Name": business.business_name,
            "User-Secret": business.business_password,
        },
    )

    return (
        jsonify(
            {
                "business_id": business.business_id,
                "business_name": business_name,
                "business_password": business.business_password,
                "token": access_token,
            }
        ),
        response.json(),
    )


@business.route("/verify/<business_verify_token>", methods=["POST"])
def login_business_for_the_first_time(business_verify_token):
    data = request.json
    business_name = data.get("business_name")
    password = data.get("business_password")
    business = Business.query.filter_by(business_name=business_name).first()

    if business is None or business_verify_token is None:
        return jsonify({"error": "Unauthorized access"}), 401

    if not bcrypt.check_password_hash(business.business_password, password):
        return jsonify({"error": "Unauthorized"}), 401

    business.business_verified = True
    db.session.commit()

    access_token = create_access_token(identity=business_name)
    session["business_id"] = business.business_id

    response = requests.get(
        "https://api.chatengine.io/users/me/",
        headers={
            "Project-ID": "7f8e7fee-521a-4f50-8d9a-9028fc529c34",
            "User-Name": request.get_json()["business_name"],
            "User-Secret": request.get_json()["business_password"],
        },
    )

    return (
        jsonify(
            {
                "business_id": business.business_id,
                "business_name": business_name,
                "business_password": business.business_password,
                "token": access_token,
            }
        ),
        response.json(),
    )
