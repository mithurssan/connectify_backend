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
        "id": user.id,
        "username": user.username,
        "password": user.password
    }

@user.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    UserController.register_user(username, password)
    return jsonify({"username":username, "password":password})
