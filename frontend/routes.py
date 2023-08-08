from flask import Blueprint, render_template

frontend_bp = Blueprint('frontend', __name__)

@frontend_bp.route('/')
def index():
    return render_template('index.html')

@frontend_bp.route('/menu')
def menu():

    menu_items = [
        {'name': 'Burger', 'description': 'Delicious burger with juicy beef patty.', 'price': 9.99},
        {'name': 'Pizza', 'description': 'Cheesy pizza with your favorite toppings.', 'price': 12.99},
        {'name': 'Pasta', 'description': 'Italian pasta with mouthwatering sauce.', 'price': 10.49},
    ]
    return render_template('menu.html', menu_items=menu_items)

@frontend_bp.route('/cart')
def cart():
    return render_template('cart.html')

@frontend_bp.route('/checkout')
def checkout():
    return render_template('checkout.html')

@frontend_bp.route('/order-history')
def order_history():
    return render_template('order_history.html')

