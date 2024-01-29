# backend/routes/order_routes.py
from flask import Blueprint, jsonify, request
from backend.models import db, Order, CartItem

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/order', methods=['GET'])
def get_order_history():
    orders = Order.query.all()
    order_data = [{'id': order.id, 'total_price': order.total_price, 'items': order.get_items()} for order in orders]
    return jsonify(order_data), 200

@order_bp.route('/order/place', methods=['POST'])
def place_order():
    data = request.get_json()
    if 'items' not in data or 'total_price' not in data:
        return jsonify({'error': 'Items and total_price are required'}), 400

    items = data['items']
    total_price = data['total_price']

    new_order = Order(total_price=total_price)
    for item in items:
        new_order.add_item(item['name'], item['price'], item['quantity'])

    db.session.add(new_order)
    db.session.commit()

    return jsonify({'message': 'Order placed successfully'}), 201

