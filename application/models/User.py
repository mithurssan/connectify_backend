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


    # def update(self):
    #     db.session.commit()
    
    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()
    
    @staticmethod
    def get_all():
        return User.query.all()

        
    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
