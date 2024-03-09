from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from db import db



#create blueprint for users_crud
products_crud = Blueprint('products_crud', __name__,
                        template_folder='templates')



class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(100), nullable=False)
    amountAvailable = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    sellerId = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Product(id={self.id}, productName='{self.productName}', amountAvailable={self.amountAvailable}, cost={self.cost}, sellerId={self.sellerId})"

@products_crud.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    output = []
    for product in products:
        product_data = {
            'id': product.id,
            'productName': product.productName,
            'amountAvailable': product.amountAvailable,
            'cost': product.cost,
            'sellerId': product.sellerId
        }
        output.append(product_data)
    return jsonify({'products': output})

@products_crud.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify({
        'id': product.id,
        'productName': product.productName,
        'amountAvailable': product.amountAvailable,
        'cost': product.cost,
        'sellerId': product.sellerId
    })

@products_crud.route('/product_create', methods=['POST'])
def create_product():
    data = request.json
    new_product = Product(
        productName=data['productName'],
        amountAvailable=data['amountAvailable'],
        cost=data['cost'],
        sellerId=data['sellerId']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully!'}), 201

@products_crud.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.json
    product.productName = data['productName']
    product.amountAvailable = data['amountAvailable']
    product.cost = data['cost']
    product.sellerId = data['sellerId']
    db.session.commit()
    return jsonify({'message': 'Product updated successfully!'})

@products_crud.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully!'})
