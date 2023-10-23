from flask import Flask, request, jsonify
from decimal import Decimal

app = Flask(__name__)

@app.route('/')
def hello():
    return "Server is available"

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    num1 = Decimal(data['num1'])
    num2 = Decimal(data['num2'])
    result = num1 + num2
    return jsonify({'result': str(result)})


@app.route('/substract', methods=['POST'])
def substract():
    data = request.get_json()
    num1 = Decimal(data['num1'])
    num2 = Decimal(data['num2'])
    result = num1 - num2
    return jsonify({'result': str(result)})


if __name__ == '__main__':
    app.run()