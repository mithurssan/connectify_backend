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


   
