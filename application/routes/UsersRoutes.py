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

@user.route('/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = UserController.get_one_by_user_id(user_id)
    if user:
        return jsonify(format_users(user))
    else:
        return jsonify({'message': 'User not found'})

@user.route('/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    username = data.get('username')
    password = data.get('password')
    UserController.update_user(user_id, username, password)
    return jsonify({"message": "User updated successfully"})

@user.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    UserController.delete_user(user_id)
    return jsonify({"message": "User deleted successfully"})

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
