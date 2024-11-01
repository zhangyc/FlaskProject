# models/comment.py

class Comment:
    def __init__(self, post_id, user_id, content):
        self.post_id = post_id
        self.user_id = user_id
        self.content = content