from flask import jsonify

def add(numberA, numberB):
    result = numberA + numberB
    return jsonify({'status': 200, 'result': result})