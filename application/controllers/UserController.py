from application.models import User
from flask import abort
import bcrypt

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
        if "user_username" in data:
            user.user_username = data["user_username"]
        if "user_password" in data:
            password = data["user_password"]
            hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
            user.user_password = hashed_password
        user.update()

    def add_user_to_business(username, data):
        user = User.query.filter_by(user_username=username).first()
        if user:
            if"user_business_name" in data:
                user.user_business_name = data["user_business_name"]
            if "business_id" in data:
                user.business_id = data["business_id"]
            user.update()
            return {"message": "User updated successfully"}
        else:
            abort(404, "User not found")

    def delete_user(user_id):
        user = User.get_by_id(user_id)
        if user:
            user.delete()
