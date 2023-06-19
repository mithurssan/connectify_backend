from application.models import User
from application import bcrypt
from flask import abort

class UserController:
    def register_user(username, email, password):
        user = User(username, email, password)
        user.save()

    def get_all_users():
        return User.get_all()

    def get_one_by_user_id(user_id):
        return User.get_by_id(user_id)

    def update_user(user_id, data):
        user = User.get_by_id(user_id)
        if "user_email" in data:
            user.user_email = data["user_email"]
        elif "user_username" in data:
            user.user_username = data["user_username"]
        elif "user_password" in data:
            user.user_password = data["user_password"]
        user.update()
    
    def add_user_to_business(username, data):
        user = User.query.filter_by(user_username=username).first()
        if user:
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
