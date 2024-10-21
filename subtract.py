from flask import jsonify
def subtract(numberA, numberB):   
   result = numberA - numberB
   return jsonify({'status': 200, 'result': result})