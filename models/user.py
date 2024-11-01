# models/user.py

from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, username, password, email, role='user',_id=None):
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.email = email
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

