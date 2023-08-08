from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Menu page
@app.route('/menu')
def menu():
    # Replace this with logic to fetch menu items from the backend and pass them to the template
    # For this example, we'll just pass a sample list of menu items
    menu_items = [
        {'name': 'Burger', 'description': 'Delicious burger with juicy beef patty.', 'price': 9.99},
        {'name': 'Pizza', 'description': 'Cheesy pizza with your favorite toppings.', 'price': 12.99},
        {'name': 'Pasta', 'description': 'Italian pasta with mouthwatering sauce.', 'price': 10.49},
    ]
    return render_template('menu.html', menu_items=menu_items)

# Cart page
@app.route('/cart')
def cart():
    return render_template('cart.html')

# Checkout page
@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

# Order History page
@app.route('/order-history')
def order_history():
    return render_template('order_history.html')

if __name__ == '__main__':
    app.run(debug=True)

