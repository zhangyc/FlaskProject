# app.py

from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mongo = PyMongo(app)
jwt = JWTManager(app)
CORS(app)

# 注册蓝图
from routes.auth import auth_bp
from routes.post import post_bp
from routes.comment import comment_bp

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(post_bp, url_prefix='/api/posts')
app.register_blueprint(comment_bp, url_prefix='/api/comments')

if __name__ == '__main__':
    app.run(debug=True)