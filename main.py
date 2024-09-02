from flask import Flask, request, jsonify

app = Flask(__name__)

def add(num1, num2):
    return num1 + num2

def subtract(a, b):
    return num1 - num2

def multiply(a, b):
    return num1 * num2

def divide(num1, num2):
    if b != 0:
        return num1 / num2
    else:
        return "Not divided by zero"
    
@app.route('/add', methods=['GET'])
def add_numbers():
    num1 = float(request.args.get('num1'))
    b = float(request.args.get('num2'))
    result = add(num1, num2)
    return jsonify(result=result)

@app.route('/subtract', methods=['GET'])
def subtract_numbers():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = subtract(num1, num2)
    return jsonify(result=result)

@app.route('/multiply', methods=['GET'])
def multiply_numbers():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('b'))
    result = multiply(num1, num2)
    return jsonify(result=result)

@app.route('/divide', methods=['GET'])
def divide_numbers():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = divide(num1, num2)

    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
