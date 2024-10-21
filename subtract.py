from flask import jsonify
def multiply(numberA, numberB):   
   result = numberA * numberB
   return jsonify({'status': 200, 'result': result}