# routes/comment.py

from flask import Blueprint, request, jsonify
from app import mongo
from models.comment import Comment
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson.objectid import ObjectId

comment_bp = Blueprint('comment', __name__)

@comment_bp.route('/<post_id>', methods=['GET'])
def get_comments(post_id):
    comments = list(mongo.db.comments.find({'post_id': post_id}))
    for comment in comments:
        comment['_id'] = str(comment['_id'])
    return jsonify(comments), 200

@comment_bp.route('/<post_id>', methods=['POST'])
@jwt_required()
def add_comment(post_id):
    data = request.get_json()
    content = data.get('content')
    user_id = get_jwt_identity()

    comment = Comment(post_id, user_id, content)
    mongo.db.comments.insert_one(comment.__dict__)
    return jsonify({'msg': '评论添加成功'}), 201