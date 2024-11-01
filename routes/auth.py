# routes/auth.py

from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash

from app import mongo
from models.user import User
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if mongo.db.users.find_one({'username': username}):
        return jsonify({'msg': '用户名已存在'}), 400

    user = User(username, password, email)
    mongo.db.users.insert_one(user.__dict__)
    return jsonify({'msg': '注册成功'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user_data = mongo.db.users.find_one({'username': username})
    if user_data:
        is_correct =check_password_hash(user_data['password_hash'], password.strip())
        if is_correct:
            access_token = create_access_token(identity=user_data['username'])
            return jsonify({'access_token': access_token}), 200

    return jsonify({'msg': '用户名或密码错误'}), 401
