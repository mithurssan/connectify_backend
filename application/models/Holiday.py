from application import db

class Holiday(db.Model):
    __tablename__ = 'holiday_bookings'
    holiday_id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.business_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    holiday_start_date = db.Column(db.String(50), nullable=False)
    holiday_end_date = db.Column(db.String(50), nullable=False)
    holiday_status = db.Column(db.String(50), nullable=False)
    business = db.relationship('Business', backref='holiday_bookings')
    user = db.relationship('User', backref='holiday_bookings')

    def __init__(self, business_id, user_id, holiday_start_date, holiday_end_date, holiday_status):
        self.business_id = business_id
        self.user_id = user_id
        self.holiday_start_date = holiday_start_date
        self.holiday_end_date = holiday_end_date
        self.holiday_status = holiday_status

