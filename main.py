from flask import Flask, request, jsonify
from decimal import Decimal
import logging 

app = Flask(__name__)

# Ustawienie konfiguracji logów
logging.basicConfig(filename='requests.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Lista przechowująca instancje mikroserwisu
instances = []

# Dodanie kilku instancji
instances.append({'instance_name': 'Instance 1'})
instances.append({'instance_name': 'Instance 2'})
instances.append({'instance_name': 'Instance 3'})

# Zmienna śledząca aktualną instancję
current_instance_index = 0

@app.route('/')
def hello():
    return "Server is available"

# Funkcja pomocnicza do pobierania aktualnej instancji
def get_current_instance():
    global current_instance_index
    instance = instances[current_instance_index]
    current_instance_index = (current_instance_index + 1) % len(instances)
    return instance

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    num1 = Decimal(data['num1'])
    num2 = Decimal(data['num2'])
    current_instance = get_current_instance()

    # Dodanie logu przed przekazaniem żądania do instancji
    logging.info(f"Request - Endpoint: add, Instance: {current_instance['instance_name']}, Numbers: {num1}, {num2}")

    result = num1 + num2
    return jsonify({'instance': current_instance['instance_name'], 'result': str(result)})

@app.route('/substract', methods=['POST'])
def substract():
    data = request.get_json()
    num1 = Decimal(data['num1'])
    num2 = Decimal(data['num2'])
    current_instance = get_current_instance()
    
    # Dodanie logu przed przekazaniem żądania do instancji
    logging.info(f"Request - Endpoint: substract, Instance: {current_instance['instance_name']}, Numbers: {num1}, {num2}")

    result = num1 - num2
    return jsonify({'instance': current_instance['instance_name'], 'result': str(result)})

@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    num1 = Decimal(data['num1'])
    num2 = Decimal(data['num2'])
    current_instance = get_current_instance()

    # Dodanie logu przed przekazaniem żądania do instancji
    logging.info(f"Request - Endpoint: divide, Instance: {current_instance['instance_name']}, Numbers: {num1}, {num2}")

    result = num1 / num2
    if num2 == 0:
         return jsonify({'result': 'Błąd działania (dzielenie przez 0)'})
    else:
        result = num1 / num2
        return jsonify({'instance': current_instance['instance_name'], 'result': str(result)})

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    num1 = Decimal(data['num1'])
    num2 = Decimal(data['num2'])
    current_instance = get_current_instance()

    # Dodanie logu przed przekazaniem żądania do instancji
    logging.info(f"Request - Endpoint: multiply, Instance: {current_instance['instance_name']}, Numbers: {num1}, {num2}")

    result = num1 * num2
    return jsonify({'instance': current_instance['instance_name'], 'result': str(result)})



if __name__ == '__main__':
    app.run(debug=True)