from application import db

class Business(db.Model):
    __tablename__ = 'businesses'
    business_id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(100), nullable=False)
    business_number = db.Column(db.BigInteger, nullable=False)
    business_email = db.Column(db.String(100), nullable=False, unique=True)
    business_password = db.Column(db.String(255), nullable=False)

    def __init__(self, business_name, business_number, business_email, business_password):
        self.business_name = business_name
        self.business_number = business_number
        self.business_email = business_email
        self.business_password = business_password

