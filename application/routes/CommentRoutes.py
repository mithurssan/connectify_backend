from application.controllers import CommentController
from flask import Blueprint, abort, request, jsonify

comment = Blueprint('comment', __name__)

@comment.route('/', methods=['GET'])
def get_all_comments():
    comments = CommentController.get_all_comments()
    comment_list = []
    for comment in comments:
        comment_list.append(format_comment(comment))
    return jsonify(comment_list)

@comment.route('/<int:comment_id>', methods=['GET'])
def get_comment_by_id(comment_id):
    comment = CommentController.get_comment_by_id(comment_id)
    if comment:
        return jsonify(format_comment(comment))
    else:
        abort(404, 'Comment not found')

@comment.route('/add', methods=['POST'])
def create_comment():
    data = request.get_json()
    user_id = data['user_id']
    post_id = data['post_id']
    comment_username = data['comment_username']
    comment_content = data['comment_content']

    CommentController.create_comment(user_id, post_id, comment_username, comment_content)
    return jsonify({'message': 'Comment created.'})

@comment.route('/update/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    data = request.json
    user_id = data['user_id']
    post_id = data['post_id']
    comment_content = data['comment_content']

    CommentController.update_comment(comment_id, user_id, post_id, comment_content)
    return jsonify({"message": "Comment updated successfully"})

@comment.route('/delete/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    CommentController.delete_comment(comment_id)
    return jsonify({"message": "Comment deleted successfully"})

@comment.route('/post/<int:post_id>', methods=['GET'])
def get_comments_for_post(post_id):
    comments = CommentController.get_comments_for_post(post_id)
    comment_list = []
    for comment in comments:
        comment_list.append(format_comment(comment))
    return jsonify(comment_list)

def format_comment(comment):
    return {
        "comment_id": comment.comment_id,
        "user_id": comment.user_id,
        "post_id": comment.post_id,
        "comment_username": comment.comment_username,
        "comment_content": comment.comment_content
    }
