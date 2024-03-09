from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    deposit = db.Column(db.Float, default=0.0)
    role = db.Column(db.String(20), default='user')



from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

#create blueprint for users_crud
users_crud = Blueprint('users_crud', __name__,
                        template_folder='templates')

# Routes

@users_crud.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    new_user = User(
        username=data['username'],
        password=data['password'],
        deposit=data.get('deposit', 0.0),
        role=data.get('role', 'user')
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@users_crud.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    result = []

    for user in users:
        user_data = {
            'id': user.id,
            'username': user.username,
            'password': user.password,
            'deposit': user.deposit,
            'role': user.role
        }
        result.append(user_data)

    return jsonify({'users': result})

@users_crud.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    user_data = {
        'id': user.id,
        'username': user.username,
        'password': user.password,
        'deposit': user.deposit,
        'role': user.role
    }

    return jsonify({'user': user_data})

@users_crud.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()

    user.username = data.get('username', user.username)
    user.password = data.get('password', user.password)
    user.deposit = data.get('deposit', user.deposit)
    user.role = data.get('role', user.role)

    db.session.commit()

    return jsonify({'message': 'User updated successfully'})

@users_crud.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted successfully'})

