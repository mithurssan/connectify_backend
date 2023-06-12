from application import db

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    user_username = db.Column(db.String(100), nullable=False)
    user_password = db.Column(db.String(100), nullable=False)
    
    def __init__(self, user_username, user_password):
        self.user_username = user_username
        self.user_password = user_password

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def get_all():
        return User.query.all()


