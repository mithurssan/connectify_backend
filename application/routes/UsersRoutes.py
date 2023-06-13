from application.controllers import UserController
from application.models import User
from flask import Blueprint, request, jsonify, session
from application import bcrypt


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
        "id": user.user_id,
        "username": user.user_username,
        "password": user.user_password,
    }


@user.route("/register", methods=["POST"])
def register_user():
    data = request.json
    # print(data)
    username = data.get("user_username")
    password = data.get("user_password")

    user_exist = User.query.filter_by(user_username=username).first() is not None

    if user_exist:
        return jsonify({"error": "Username already exist"})

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = User(user_username=username, user_password=hashed_password)

    session["user_id"] = new_user.user_id

    UserController.register_user(username, hashed_password)
    return jsonify({"username": username, "password": hashed_password})


@user.route("/login", methods=["POST"])
def login_user():
    data = request.json
    # print(data)
    username = data.get("user_username")
    password = data.get("user_password")

    return jsonify({"username": username})
