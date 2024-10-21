from flask import Flask 
from operations.add import add 
from operations.minus import minus 
from operations.multiply import multiply 
from operations.divide import divide 
 
app = Flask(__name__) 
 
# Register the routes from each file 
app.add_url_rule('/add/<float:numberA>/<float:numberB>', 'add', add) 
app.add_url_rule('/minus/<float:numberA>/<float:numberB>', 'minus', minus) 
app.add_url_rule('/multiply/<float:numberA>/<float:numberB>', 'multiply', multiply) 
app.add_url_rule('/divide/<float:numberA>/<float:numberB>', 'divide', divide) 
 
if name == '__main__': 
    app.run(debug=True)