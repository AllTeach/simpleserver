from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def get_location():
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    response = f"Lat= {latitude} Long= {longitude}"
    return jsonify(response=response)

if __name__ == '__main__':
    app.run(debug=True)