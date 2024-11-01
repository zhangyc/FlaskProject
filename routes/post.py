# routes/post.py

from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

from app import mongo
from models.post import Post
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson.objectid import ObjectId

post_bp = Blueprint('post', __name__)

@post_bp.route('/', methods=['GET'])
def get_posts():
    # 正常处理 GET 请求
    posts = list(mongo.db.posts.find())
    for post in posts:
        post['_id'] = str(post['_id'])
    return jsonify(posts), 200

@post_bp.route('/<post_id>', methods=['GET'])
def get_post(post_id):
    post = mongo.db.posts.find_one({'_id': ObjectId(post_id)})
    if post:
        return jsonify(post), 200
    return jsonify({'msg': '文章不存在'}), 404

@post_bp.route('/', methods=['POST'])
@jwt_required()
def create_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    tags = data.get('tags', [])
    author_id = get_jwt_identity()

    post = Post(title, content, author_id, tags)
    mongo.db.posts.insert_one(post.__dict__)
    return jsonify({'msg': '文章创建成功'}), 200
