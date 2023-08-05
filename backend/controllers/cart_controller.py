# backend/controllers/cart_controller.py
from flask import Blueprint, jsonify, request
from backend.models import db, CartItem

cart_bp = Blueprint('cart_bp', __name__)

@cart_bp.route('/cart', methods=['GET'])
def get_cart_items():
    # Implement logic to fetch cart items for the authenticated user
    # For example:
    # user_id = get_authenticated_user_id()
    # cart_items = CartItem.query.filter_by(user_id=user_id).all()
    cart_items = CartItem.query.all()
    cart_data = [{'id': item.id, 'name': item.name, 'price': item.price, 'quantity': item.quantity} for item in cart_items]
    return jsonify(cart_data), 200

@cart_bp.route('/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    if 'name' not in data or 'price' not in data or 'quantity' not in data:
        return jsonify({'error': 'Name, price, and quantity are required'}), 400

    name = data['name']
    price = data['price']
    quantity = data['quantity']

    # Implement logic to add item to the authenticated user's cart
    # For example:
    # user_id = get_authenticated_user_id()
    # cart_item = CartItem(name=name, price=price, quantity=quantity, user_id=user_id)
    cart_item = CartItem(name=name, price=price, quantity=quantity)

    db.session.add(cart_item)
    db.session.commit()

    return jsonify({'message': 'Item added to cart'}), 201

@cart_bp.route('/cart/<int:item_id>', methods=['DELETE'])
def remove_from_cart(item_id):
    # Implement logic to remove item from the authenticated user's cart by item_id
    # For example:
    # user_id = get_authenticated_user_id()
    # cart_item = CartItem.query.filter_by(user_id=user_id, id=item_id).first()
    cart_item = CartItem.query.get(item_id)

    if not cart_item:
        return jsonify({'error': 'Item not found in cart'}), 404

    db.session.delete(cart_item)
    db.session.commit()

    return jsonify({'message': 'Item removed from cart'}), 200
