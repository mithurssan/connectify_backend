from application.models import Post
from application import db

class PostController:
    def create_post(user_id, business_id, username, post_title, post_content):
        post = Post(user_id, business_id, username, post_title, post_content)
        post.save()

    def get_all_posts():
        return Post.get_all()

    def get_one_by_post_id(post_id):
        return Post.get_by_id(post_id)
    
    def get_posts_from_business(business_id):
        return Post.get_posts_from_business(business_id)

    def update_post(post_id, data):
        post = Post.get_by_id(post_id)
        if "user_id" in data:
            post.user_id = data["user_id"]
        if "business_id" in data:
            post.business_id = data["business_id"]
        if "post_title" in data:
            post.post_title = data["post_title"]
        if "post_content" in data:
            post.post_content = data["post_content"]
        post.update()

    def upvote_post(post_id):
        post = db.session.get(Post, post_id)
        post.upvote()
    
    def cancel_upvote_post(post_id):
        post = db.session.get(Post, post_id)
        post.cancel_upvote()
    
    def downvote_post(post_id):
        post = db.session.get(Post, post_id)
        post.downvote()

    def delete_post(post_id):
        post = Post.get_by_id(post_id)
        if post:
            post.delete()
