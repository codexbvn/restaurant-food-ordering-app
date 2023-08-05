# backend/controllers/order_controller.py
from flask import Blueprint, jsonify, request
from backend.models import db, Order

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/order', methods=['GET'])
def get_order_history():
    # Implement logic to fetch order history for the authenticated user
    # For example:
    # user_id = get_authenticated_user_id()
    # orders = Order.query.filter_by(user_id=user_id).all()
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

    # Implement logic to place the order for the authenticated user
    # For example:
    # user_id = get_authenticated_user_id()
    # new_order = Order(total_price=total_price, user_id=user_id)
    # for item in items:
    #     new_order.add_item(item['name'], item['price'], item['quantity'])

    new_order = Order(total_price=total_price)
    for item in items:
        new_order.add_item(item['name'], item['price'], item['quantity'])

    db.session.add(new_order)
    db.session.commit()

    return jsonify({'message': 'Order placed successfully'}), 201
