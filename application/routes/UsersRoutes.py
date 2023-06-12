from application.controllers import UserController
from flask import Blueprint, request
from flask import jsonify
user = Blueprint('user', __name__)

@user.route('/')
def get_users():
    users = UserController.get_all_users()
    user_list=[]
    for user in users:
        user_list.append(format_users(user))
    return jsonify(user_list)

def format_users(user):
    return {
        "id": user.user_id,
        "username": user.user_username,
        "password": user.user_password
    }

@user.route('/register', methods=['POST'])
def register():
    data = request.json
    print(data)
    username = data.get('user_username')
    password = data.get('user_password')
    UserController.register_user(username, password)
    return jsonify({"username":username, "password":password})
