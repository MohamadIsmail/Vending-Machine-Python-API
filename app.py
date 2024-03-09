from flask import Flask, request, jsonify
from users import users_crud
from products import products_crud
from users import User
from utils import app
from db import db


app.register_blueprint(users_crud)

app.register_blueprint(products_crud)

@app.route("/", methods=['GET'])
def alive():
    return jsonify({"message":"alive"})


# Deposit endpoint
@app.route('/deposit', methods=['POST'])
def deposit():
    data = request.json
    username = data.get("username")
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "User not found"}), 404
    if not user.role=="buyer":
        return jsonify({"message": "Unauthorized"}), 401
    amount = data.get("amount")
    if amount not in [5, 10, 20, 50, 100]:
        return jsonify({"message": "Invalid coin"}), 400
   
    user["deposit"] += amount
    db.session.commit()
    return jsonify({"message": "Deposit successful", "deposit": user["deposit"]})

# Buy endpoint
@app.route('/buy', methods=['POST'])
def buy():
    data = request.json
    username = data.get("username")
    if not is_buyer(username):
        return jsonify({"message": "Unauthorized"}), 401
    product_id = data.get("productId")
    amount = data.get("amount")
    product = next((product for product in products if product["productId"] == product_id), None)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    total_cost = product["cost"] * amount
    for user in users:
        if user["username"] == username:
            if user["deposit"] < total_cost:
                return jsonify({"message": "Insufficient funds"}), 400
            user["deposit"] -= total_cost
            product["amountAvailable"] -= amount
            return jsonify({
                "message": "Purchase successful",
                "total_spent": total_cost,
                "products_purchased": [{"productName": product["productName"], "amount": amount}],
                "change": user["deposit"]
            })

# Reset deposit endpoint
@app.route('/reset', methods=['POST'])
def reset_deposit():
    data = request.json
    username = data.get("username")
    if not is_buyer(username):
        return jsonify({"message": "Unauthorized"}), 401
    for user in users:
        if user["username"] == username:
            user["deposit"] = 0
            return jsonify({"message": "Deposit reset successful", "deposit": user["deposit"]})
    return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
