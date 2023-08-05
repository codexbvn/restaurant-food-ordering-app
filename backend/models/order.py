# backend/models/order.py
from . import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_price = db.Column(db.Float, nullable=False)
    items = db.relationship('CartItem', backref='order', lazy=True)

    def __init__(self, total_price):
        self.total_price = total_price

    def add_item(self, name, price, quantity):
        item = CartItem(name=name, price=price, quantity=quantity, order=self)
        db.session.add(item)
        db.session.commit()

    def get_items(self):
        return [{'id': item.id, 'name': item.name, 'price': item.price, 'quantity': item.quantity} for item in self.items]
