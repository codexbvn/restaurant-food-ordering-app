# restaurant-food-ordering-app

# Restaurant Food Ordering Web Application

This project is a web application for a restaurant food ordering system. It allows users to browse the restaurant's menu, add items to their cart, and place orders. The application is built using the Flask framework for the backend and HTML, CSS, and JavaScript for the frontend.

## Features

- User authentication: Users can create accounts and log in to the application.
- Menu display: The application displays the restaurant's menu items with their names, descriptions, and prices.
- Cart management: Users can add menu items to their cart, view the items in the cart, and remove items from the cart.
- Order placement: Authenticated users can place orders for the items in their cart.
- Order history: Users can view their order history and see the details of their previous orders.

## File Hierarchy

restaurant-food-ordering-app/ 
|-- backend/ 
|   |-- app.py 
|   |-- config.py 
|   |-- database.db 
|   |-- controllers/ 
|   |   |-- __init__.py 
|   |   |-- auth_controller.py 
|   |   |-- cart_controller.py 
|   |   |-- menu_controller.py 
|   |   |-- order_controller.py 
|   |-- models/ 
|   |   |-- __init__.py 
|   |   |-- cart_item.py 
|   |   |-- menu_item.py 
|   |   |-- order.py 
|   |   |-- user.py 
|   |-- routes/ 
|   |   |-- __init__.py 
|   |   |-- auth_routes.py 
|   |   |-- cart_routes.py 
|   |   |-- menu_routes.py 
|   |   |-- order_routes.py 
|-- frontend/ 
|   |-- app.py 
|   |-- static/ 
|   |   |-- css/ 
|   |   |   |-- style.css 
|   |   |-- js/ 
|   |   |   |-- script.js 
|   |-- templates/ 
|   |   |-- base.html 
|   |   |-- cart.html 
|   |   |-- checkout.html 
|   |   |-- index.html 
|   |   |-- menu.html 
|   |   |-- order_history.html 
|-- run.py 

## Dependencies


Flask

Flask-CORS

Flask-WTF

Flask-Login

Flask-SQLAlchemy



