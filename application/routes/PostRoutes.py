from application.controllers import PostController
from flask import Blueprint, abort, request
from flask import jsonify
post = Blueprint('post', __name__)

@post.route('/', methods=["GET"])
def get_users():
    posts = PostController.get_all_posts()
    post_list=[]
    for post in posts:
        post_list.append(format_posts(post))
    return jsonify(post_list)

def format_posts(post):
    return {
        "post_id": post.post_id,
        "user_id": post.user_id,
        "business_id": post.business_id,
        "username": post.username,
        "post_title": post.post_title,
        "post_content": post.post_content,
        "post_upvotes": post.post_upvotes,
        "post_downvotes": post.post_downvotes
    }

@post.route('/add', methods=['POST'])
def create_post():
    data = request.get_json()
    user_id = data['user_id']
    business_id = data['business_id']
    username = data["username"]
    post_title = data['post_title']
    post_content = data['post_content']

    PostController.create_post(user_id, business_id, username, post_title, post_content)
    return jsonify({'message': 'Post created.'})

@post.route('/<post_id>', methods=['GET'])
def get_user_by_id(post_id):
    post = PostController.get_one_by_post_id(post_id)
    if post:
        return jsonify(format_posts(post))
    else:
        abort(404, 'Post not found')

@post.route("/get/<string:business_id>", methods=["GET"])
def get_posts_from_business(business_id):
    posts = PostController.get_posts_from_business(business_id)
    post_list=[]
    for post in posts:
        post_list.append(format_posts(post))
    return jsonify(post_list)

@post.route('/update/<int:post_id>', methods=['PATCH'])
def update_post(post_id):
    data = request.json
    PostController.update_post(post_id, data)
    return jsonify({"message": "Post updated successfully"})

@post.route('/update/<int:post_id>/upvote', methods=['PATCH'])
def upvote_post(post_id):
    PostController.upvote_post(post_id)
    return jsonify({"message": "Post upvoted successfully"})

@post.route('/update/<int:post_id>/cancel_upvote', methods=['PATCH'])
def cancel_upvote_post(post_id):
    PostController.cancel_upvote_post(post_id)
    return jsonify({"message": "Post cancelled upvote successfully"})

@post.route('/update/<int:post_id>/downvote', methods=['PATCH'])
def downvote_post(post_id):
    PostController.downvote_post(post_id)
    return jsonify({"message": "Post downvoted successfully"})

@post.route('/delete/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    PostController.delete_post(post_id)
    return jsonify({"message": "Post deleted successfully"})
