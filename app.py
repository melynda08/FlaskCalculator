from flask import Flask, jsonify
from add import add  # Import the addition function

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to the Flask Calculator!"

# Addition route
@app.route('/add/<int:numberA>/<int:numberB>')  # Use <int:> to ensure numbers are passed as integers
def add_route(numberA, numberB):
    return add(numberA, numberB)

# Additional routes for other operations can be added similarly
# Example for subtraction
from minus import minus  # Import subtraction function
@app.route('/minus/<int:numberA>/<int:numberB>')
def minus_route(numberA, numberB):
    return minus(numberA, numberB)

# Example for multiplication
from multiply import multiply  # Import multiplication function
@app.route('/multiply/<int:numberA>/<int:numberB>')
def multiply_route(numberA, numberB):
    return multiply(numberA, numberB)

# Example for division
from devide import divide  # Import division function
@app.route('/divide/<int:numberA>/<int:numberB>')
def divide_route(numberA, numberB):
    return divide(numberA, numberB)

if __name__ == '__main__':
    app.run(debug=True)
