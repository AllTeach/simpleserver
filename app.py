from flask import Flask, jsonify
import csv
import random

app = Flask(__name__)

def get_city_by_line(line_number):
    with open('worldcities.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for current_line, row in enumerate(reader, start=1):
            if current_line == line_number:
                return row
    return None

@app.route('/')
def get_location():
    random_line = random.randint(2, 47869)
    city = get_city_by_line(random_line)
    if city:
        latitude = city[2]
        longitude = city[3]
        response = f"Lat= {latitude} Long= {longitude}"
        return jsonify(response=response)
    return jsonify(response="City not found"), 404

if __name__ == '__main__':
    app.run(debug=True)