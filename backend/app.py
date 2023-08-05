from flask import Flask
from flask_cors import CORS
from backend.models import db
from backend.routes.auth_routes import auth_bp
from backend.routes.cart_routes import cart_bp
from backend.routes.menu_routes import menu_bp
from backend.routes.order_routes import order_bp
from backend.config import Config

app = Flask(__name__)

# Set up the app configuration
app.config.from_object(Config)

# Set up the database
db.init_app(app)

# Enable Cross-Origin Resource Sharing (CORS)
CORS(app)

# Register blueprints for different routes
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(cart_bp, url_prefix='/api')
app.register_blueprint(menu_bp, url_prefix='/api')
app.register_blueprint(order_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
