from application import db
from uuid import uuid4


def get_uuid():
    return uuid4().hex


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    business_id = db.Column(db.String(32), db.ForeignKey("businesses.business_id"), nullable=True)
    user_username = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    user_password = db.Column(db.String(100), nullable=False)
    user_verify_token = db.Column(db.String(32), nullable=False)
    user_verified = db.Column(db.Boolean(), nullable=False)


    business = db.relationship("Business", backref="users")
    journal_entries = db.relationship('Journal', back_populates='users')


    def __init__(
        
        self, user_username, user_email, user_password, user_verify_token, user_verified
    ):
        self.user_username = user_username
        self.user_email = user_email
        self.user_password = user_password
        self.user_verify_token = user_verify_token
        self.user_verified = user_verified

    @staticmethod
    def get_all():
        return User.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(user_id):
        return db.session.get(User, user_id)

    @staticmethod
    def get_by_token(user_verify_token):
        return db.session.get(User, user_verify_token)

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
