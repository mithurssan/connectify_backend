from application import db
from uuid import uuid4


def get_uuid():
    return uuid4().hex


class Business(db.Model):
    __tablename__ = "businesses"
    business_id = db.Column(
        db.String(32), primary_key=True, unique=True, default=get_uuid
    )
    business_name = db.Column(db.String(100), nullable=False)
    business_password = db.Column(db.String(255), nullable=False)
    business_email = db.Column(db.String(100), nullable=False, unique=True)
    business_number = db.Column(db.Integer, nullable=False)

    def __init__(
        self, business_name, business_password, business_email, business_number
    ):
        self.business_name = business_name
        self.business_password = business_password
        self.business_email = business_email
        self.business_number = business_number

    @staticmethod
    def get_all():
        return Business.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(business_id):
        return Business.query.get(business_id)

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
