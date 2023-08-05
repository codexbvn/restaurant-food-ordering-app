# backend/routes/menu_routes.py
from flask import Blueprint, jsonify, request
from backend.models import db, MenuItem

menu_bp = Blueprint('menu_bp', __name__)

@menu_bp.route('/menu', methods=['GET'])
def get_menu_items():
    menu_items = MenuItem.query.all()
    menu_data = [{'id': item.id, 'name': item.name, 'price': item.price} for item in menu_items]
    return jsonify(menu_data), 200

@menu_bp.route('/menu/add', methods=['POST'])
def add_menu_item():
    data = request.get_json()
    if 'name' not in data or 'price' not in data:
        return jsonify({'error': 'Name and price are required'}), 400

    name = data['name']
    price = data['price']

    menu_item = MenuItem(name=name, price=price)

    db.session.add(menu_item)
    db.session.commit()

    return jsonify({'message': 'Menu item added successfully'}), 201

@menu_bp.route('/menu/<int:item_id>', methods=['DELETE'])
def remove_menu_item(item_id):
    menu_item = MenuItem.query.get(item_id)

    if not menu_item:
        return jsonify({'error': 'Menu item not found'}), 404

    db.session.delete(menu_item)
    db.session.commit()

    return jsonify({'message': 'Menu item removed successfully'}), 200
