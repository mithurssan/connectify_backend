from application.models import Comment

class CommentController:
    def create_comment(user_id, post_id, comment_content):
        comment = Comment(user_id, post_id, comment_content)
        comment.save()

    def get_all_comments():
        return Comment.get_all()

    def get_comment_by_id(comment_id):
        return Comment.get_by_id(comment_id)
    
    def get_comments_for_post(post_id):
        return Comment.get_comments_for_post(post_id)
    
    def update_comment(comment_id, user_id, post_id, comment_content):
        comment = Comment.get_by_id(comment_id)
        if comment:
            comment.user_id = user_id
            comment.post_id = post_id
            comment.comment_content = comment_content
            comment.update()

    def delete_comment(comment_id):
        comment = Comment.get_by_id(comment_id)
        if comment:
            comment.delete()
