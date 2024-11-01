# models/post.py

class Post:
    def __init__(self, title, content, author_id, tags=[]):
        self.title = title
        self.content = content
        self.author_id = author_id
        self.tags = tags