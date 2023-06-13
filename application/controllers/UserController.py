from application.models import User

class UserController:
    @staticmethod
    def register_user(username, password):
        user = User(username, password)
        user.save()

    def get_all_users():
        return User.get_all()

    @staticmethod
    def get_one_by_user_id(user_id):
        return User.get_by_id(user_id)

    @staticmethod
    def update_user(user_id, username, password):
        user = User.get_by_id(user_id)
        if user:
            user.username = username
            user.password = password
            user.update()

    def delete_user(user_id):
        user = User.get_by_id(user_id)
        if user:
            user.delete()
