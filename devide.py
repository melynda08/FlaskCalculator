from flask import jsonify

def divide(numberA, numberB):
    try:
        result = numberA / numberB
        return jsonify({'status': 200, 'result': result})
    except ZeroDivisionError:
        return jsonify({'status': 400, 'error': 'Division by zero is not allowed.'}), 400
