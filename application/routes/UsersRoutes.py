import json
import requests
from os import environ
from application.controllers import UserController
from application.models import User
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

user = Blueprint("user", __name__)


@user.route("/")
def get_users():
    users = UserController.get_all_users()
    user_list = []
    for user in users:
        user_list.append(format_users(user))
    return jsonify(user_list), 200


def format_users(user):
    return {
        "user_id": user.user_id,
        "user_username": user.user_username,
        "user_email": user.user_email,
        "user_password": user.user_password,
        "user_verify_token": user.user_verify_token,
        "user_verified": user.user_verified,
    }


@user.route("/<user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user = UserController.get_one_by_user_id(user_id)
    if user:
        return jsonify(format_users(user))
    else:
        return jsonify({"message": "User not found"}), 404


@user.route("/update/<string:user_id>", methods=["PATCH"])
def update_user(user_id):
    data = request.json
    UserController.update_user(user_id, data)
    return jsonify({"message": "User updated successfully"})

@user.route("/update/business/<string:username>", methods=["PATCH"])
def add_user_to_business(username):
    data = request.json
    response = UserController.add_user_to_business(username, data)
    return jsonify(response)

@user.route("/delete/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    UserController.delete_user(user_id)
    return jsonify({"message": "User deleted successfully"})


@user.route("/register", methods=["POST"])
def register_user():
    data = request.json

    username = data.get("user_username")
    email = data.get("user_email")
    password = data.get("user_password")
    verify_token = uuid4().hex
    verified = False

    user_exist = User.query.filter_by(user_username=username).first() is not None
    if user_exist:
        return jsonify({"error": "Username already exist"})
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = User(
        user_username=username,
        user_email=email,
        user_password=hashed_password,
        user_verify_token=verify_token,
        user_verified=verified,
    )

    session["user_id"] = new_user.user_id

    UserController.register_user(
        username, email, hashed_password, verify_token, verified
    )

    send_verification_email(email, verify_token)

    response = requests.post(
        "https://api.chatengine.io/users/",
        data={
            "username": request.get_json()["user_username"],
            "secret": hashed_password,
            "email": request.get_json()["user_email"],
        },
        headers={"Private-Key": "7f306ed8-bf91-4841-b5e1-f9bf00e39ddf"},
    )

    return (
        jsonify(
            {
                "username": username,
                "email": email,
                "password": hashed_password,
                "verify_token": verify_token,
                "verified": verified,
            }
        ),
        response.json(),
    )


def send_verification_email(email, verify_token):
    verification_link = f"http://localhost:5173/users/verify/{verify_token}"

    mail.send_message(
        "USER - Verify your email",
        sender=environ.get("EMAIL"),
        recipients=[email],
        body=f"Click the following link to verify your email: {verification_link}",
    )


@user.after_request
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


@user.route("/login", methods=["POST"])
def login_user():
    data = request.json
    user_username = data.get("user_username")
    password = data.get("user_password")

    user = User.query.filter_by(user_username=user_username).first()

    if user is None:
        return jsonify({"error": "Unauthorized access"}), 401

    if not bcrypt.check_password_hash(user.user_password, password):
        return jsonify({"error": "Unauthorized"}), 401

    access_token = create_access_token(identity=user_username, additional_claims={"user_id": user.user_id})
    session["user_id"] = user.user_id

    response = requests.get(
        "https://api.chatengine.io/users/me/",
        headers={
            "Project-ID": environ.get("CHAT_ENGINE_PROJECT_ID"),
            "User-Name": user.user_username,
            "User-Secret": user.user_password,
        },
    )

    return (
        jsonify(
            {"user_id": user.user_id, "business_id": user.business_id, "username": user_username, "token": access_token, "password": password}
        ),
        response.json(),
    )


@user.route("/verify/<user_verify_token>", methods=["POST"])
def login_user_for_the_first_time(user_verify_token):
    data = request.json
    user_username = data.get("user_username")
    password = data.get("user_password")
    user = User.query.filter_by(user_username=user_username).first()

    if user is None or user_verify_token is None:
        return jsonify({"error": "Unauthorized access"}), 401

    if not bcrypt.check_password_hash(user.user_password, password):
        return jsonify({"error": "Unauthorized"}), 401

    user.user_verified = True
    db.session.commit()

    access_token = create_access_token(identity=user_username)
    session["user_id"] = user.user_id

    response = requests.get(
        "https://api.chatengine.io/users/me/",
        headers={
            "Project-ID": "7f8e7fee-521a-4f50-8d9a-9028fc529c34",
            "User-Name": request.get_json()["user_username"],
            "User-Secret": request.get_json()["user_password"],
        },
    )

    return jsonify({"username": user_username, "token": access_token}), response.json()
