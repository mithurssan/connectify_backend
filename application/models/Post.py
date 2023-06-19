from application import db

class Post(db.Model):
    __tablename__ = "posts"
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32), db.ForeignKey("users.user_id"), nullable=True)
    business_id = db.Column(db.String(32), db.ForeignKey("businesses.business_id"), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    post_title = db.Column(db.String(50), nullable=False)
    post_content = db.Column(db.String(1000), nullable=False)
    upvotes = db.Column(db.Integer, default=0)
    downvotes = db.Column(db.Integer, default=0)
    comments = db.relationship('Comment', backref='posts', lazy=True)

    def __init__(self, user_id, business_id, username, post_title, post_content):
        self.user_id = user_id
        self.business_id = business_id
        self.username = username
        self.post_title = post_title
        self.post_content = post_content

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Post.query.all()

    @staticmethod
    def get_by_id(post_id):
        return db.session.get(Post, post_id)

    @staticmethod
    def get_posts_from_business(business_id):
        print(business_id)
        return Post.query.filter_by(business_id=business_id).all()
    
    def update(self):
        db.session.commit()

    def upvote(self):
        self.upvotes += 1
        self.update()

    def downvote(self):
        self.downvotes += 1
        self.update()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

