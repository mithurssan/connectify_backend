from application import db

class Comment(db.Model):
    __tablename__ = "comments"
    comment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32), db.ForeignKey("users.user_id"), nullable=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.post_id"), nullable=False)
    comment_username = db.Column(db.String(50), nullable=False)
    comment_content = db.Column(db.String(500), nullable=False)

    def __init__(self, user_id, post_id, comment_username, comment_content):
        self.user_id = user_id
        self.post_id = post_id
        self.comment_username = comment_username
        self.comment_content = comment_content

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Comment.query.all()
    
    @staticmethod
    def get_by_id(comment_id):
        return db.session.get(Comment, comment_id)
    
    @staticmethod
    def get_comments_for_post(post_id):
        return Comment.query.filter_by(post_id=post_id).order_by(Comment.comment_id.desc()).all()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
