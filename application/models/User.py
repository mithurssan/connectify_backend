from application import db
from uuid import uuid4


def get_uuid():
    return uuid4().hex


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    user_username = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    user_password = db.Column(db.String(100), nullable=False)

    def __init__(self, user_username, user_email, user_password):
        self.user_username = user_username
        self.user_email = user_email
        self.user_password = user_password

    @staticmethod
    def get_all():
        return User.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
