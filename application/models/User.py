from application import db
from uuid import uuid4


def get_uuid():
    return uuid4().hex


# default=get_uuid -> add to user_id, change to db.String(11)
class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    user_username = db.Column(db.String(100), nullable=False)
    user_password = db.Column(db.String(100), nullable=False)

    def __init__(self, user_username, user_password):
        self.user_username = user_username
        self.user_password = user_password

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()
