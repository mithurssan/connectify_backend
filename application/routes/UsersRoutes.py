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


@user.route('/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = UserController.get_one_by_user_id(user_id)
    if user:
        return jsonify(format_users(user))
    else:
        return jsonify({'message': 'User not found'})



@user.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    UserController.register_user(username, password)
    return jsonify({"username":username, "password":password})





@user.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    UserController.delete_user(user_id)
    return jsonify({"message": "User deleted successfully"})

