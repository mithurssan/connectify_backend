from application.models import User
from application import bcrypt


class UserController:
    def register_user(username, email, password, verify_token, verified):
        user = User(username, email, password, verify_token, verified)
        user.save()

    def get_all_users():
        return User.get_all()

    def get_one_by_user_id(user_id):
        return User.get_by_id(user_id)

    def get_one_by_user_verify_token(user_verify_token):
        return User.get_by_token(user_verify_token)

    def update_user(user_id, data):
        user = User.get_by_id(user_id)
        if "user_email" in data:
            user.user_email = data["user_email"]
        elif "user_username" in data:
            user.user_username = data["user_username"]
        elif "user_password" in data:
            user.user_password = data["user_password"]
        user.update()

    def delete_user(user_id):
        user = User.get_by_id(user_id)
        if user:
            user.delete()
