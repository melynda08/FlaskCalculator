from flask import jsonify
def minus(numberA, numberB):  
    result = numberA - numberB
    return jsonify({'status': 200, 'result': result})
