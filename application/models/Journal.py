from application import db

class Journal(db.Model):
    __tablename__ = "journal_entries"
    entry_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32), db.ForeignKey("users.user_id"), nullable=False)
    entry_date = db.Column(db.String(50), nullable=False)
    entry_title = db.Column(db.String(50), nullable=False)
    entry_content = db.Column(db.String(350), nullable=False)

    def __init__(self, user_id, entry_date, entry_title, entry_content):
        self.user_id = user_id
        self.entry_date = entry_date
        self.entry_title = entry_title
        self.entry_content = entry_content

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Journal.query.all()

    @staticmethod
    def get_by_id(entry_id):
        return db.session.get(Journal, entry_id)

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

