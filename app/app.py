from typing import List, Dict
from flask import Flask
from prometheus_client import Summary, Gauge, Counter, generate_latest, REGISTRY, Histogram
import random
import mysql.connector
import json

app = Flask(__name__)
PYTHON_RANDOM_VALUE = Gauge('python_random_value', 'randomly generated in python')


def favorite_colors() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'knights'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM favorite_colors')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'favorite_colors': favorite_colors()})


@app.route('/random')
def randomPage():
    PYTHON_RANDOM_VALUE.set(random.random())
    return ("Random Page")


@app.route('/metrics', methods=['GET'])
def stats():
    return generate_latest(REGISTRY), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0')

