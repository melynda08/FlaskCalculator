from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/add/<int:numberA>/<int:numberB>', methods=['GET'])
def add(numberA, numberB):
    result = numberA + numberB
    return jsonify({'status': 200, 'result': result})

@app.route('/subtract/<int:numberA>/<int:numberB>', methods=['GET'])
def subtract(numberA, numberB):
    result = numberA - numberB
    return jsonify({'status': 200, 'result': result})

@app.route('/multiply/<int:numberA>/<int:numberB>', methods=['GET'])
def multiply(numberA, numberB):
    result = numberA * numberB
    return jsonify({'status': 200, 'result': result})

@app.route('/divide/<int:numberA>/<int:numberB>', methods=['GET'])
def divide(numberA, numberB):
    if numberB == 0:
        return jsonify({'status': 400, 'error': 'Division by zero is not allowed'})
    result = numberA / numberB
    return jsonify({'status': 200, 'result': result})

if __name__ == '__main__':
    app.run(debug=True)
