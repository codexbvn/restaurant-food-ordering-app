# backend/models/cart_item.py
from . import db

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
