import json
from application.controllers import UserController
from application.models import User
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
user = Blueprint("user", __name__)

@user.route("/")
@jwt_required()
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
    # print(data)
    username = data.get("user_username")
    email = data.get("user_email")
    password = data.get("user_password")

    user_exist = User.query.filter_by(user_username=username).first() is not None

    if user_exist:
        return jsonify({"error": "Username already exist"})

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = User(
        user_username=username, user_email=email, user_password=hashed_password
    )

    session["user_id"] = new_user.user_id

    UserController.register_user(username, email, hashed_password)
    return jsonify({"user_username": username, "user_email": email, "user_password": hashed_password})

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
    access_token = create_access_token(identity=user_username)
    session["user_id"] = user.user_id

    return jsonify({"user_id": user.user_id, "business_id": user.business_id, "user_name": user_username, "token": access_token})
