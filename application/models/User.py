import json
from application import db
from uuid import uuid4


def get_uuid():
    return uuid4().hex


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    user_business_name = db.Column(db.String(50), nullable=True)
    business_id = db.Column(
        db.String(32), db.ForeignKey("businesses.business_id"), nullable=True
    )
    user_username = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    user_password = db.Column(db.String(100), nullable=False)
    user_verify_token = db.Column(db.String(32), nullable=False)
    user_verified = db.Column(db.Boolean(), nullable=False)
    upvoted_posts = db.Column(db.String, nullable=True, default='[]')

    business = db.relationship("Business", backref="users")
    journal_entries = db.relationship("Journal", back_populates="users")

    def __init__(
        self,
        user_username,
        user_email,
        user_password,
        user_verify_token,
        user_verified,
        upvoted_posts=None
    ):
        self.user_username = user_username
        self.user_email = user_email
        self.user_password = user_password
        self.user_verify_token = user_verify_token
        self.user_verified = user_verified
        self.upvoted_posts = upvoted_posts

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

    def upvote_post(self, post_id):
        upvoted_posts = json.loads(self.upvoted_posts)
        if post_id not in upvoted_posts:
            upvoted_posts.append(post_id)
            self.upvoted_posts = json.dumps(upvoted_posts)
            db.session.commit()

    def cancel_upvote_post(self, post_id):
        upvoted_posts = json.loads(self.upvoted_posts)
        if post_id in upvoted_posts:
            upvoted_posts.remove(post_id)
            self.upvoted_posts = json.dumps(upvoted_posts)
            db.session.commit()
