from application.models import Post

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

    def update_post(post_id, user_id, business_id, post_title, post_content):
        post = Post.get_by_id(post_id)
        if post:
            post.user_id = user_id
            post.business_id = business_id
            post.post_title = post_title
            post.post_content = post_content
            post.update()

    def delete_post(post_id):
        post = Post.get_by_id(post_id)
        if post:
            post.delete()
