from application import db
from . import Business

class Rota(db.Model):
    __tablename__ = "rotas"
    rota_id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.String(32), db.ForeignKey("businesses.business_id"), nullable=False)
    rota_start_date = db.Column(db.String(50), nullable=False)
    rota_end_date = db.Column(db.String(50), nullable=False)
    rota_content = db.Column(db.String(350), nullable=False)
    business = db.relationship("Business", backref="rotas")

    def __init__(self, business_id, rota_start_date, rota_end_date, rota_content):
        self.business_id = business_id
        self.rota_start_date = rota_start_date
        self.rota_end_date = rota_end_date
        self.rota_content = rota_content

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Rota.query.all()

    @staticmethod
    def get_by_id(rota_id):
        return db.session.get(Rota, rota_id)

    @staticmethod
    def get_all_by_business_id(business_id):
        query = Rota.query.filter_by(business_id=business_id)
        return query.all()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

