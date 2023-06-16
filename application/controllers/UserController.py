from application.models import User

class UserController:
    def register_user(username, email, password):
        user = User(username, email, password)
        user.save()

    def get_all_users():
        return User.get_all()

    def get_one_by_user_id(user_id):
        return User.get_by_id(user_id)

    def update_user(user_id, user_username, user_email, user_password):
        user = User.get_by_id(user_id)
        if user:
            user.user_username = user_username
            user.user_email = user_email
            user.user_password = user_password
            user.update()

    def delete_user(user_id):
        user = User.get_by_id(user_id)
        if user:
            user.delete()
