from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)

@app.route('/get_unique_values', methods=['GET'])
def get_unique_values():
    response = {
        "suburbs": util.get_suburbs(),
        "property_types": util.get_types(),
        "region_names": util.get_region_names(),
    }
    return jsonify(response)


@app.route('/predict_price', methods=['POST'])
def predict_price():
    rooms = int(request.form['rooms'])
    distance = float(request.form['distance'])
    bathroom = int(request.form['bathroom'])
    car = int(request.form['car'])
    landsize = float(request.form['landsize'])
    suburb = request.form['suburb']
    property_type = request.form['property_type']
    region_name = request.form['region_name']

    response = {
        'estimated_price': util.predict_price(rooms, distance, bathroom, car, landsize, suburb, property_type,
                                              region_name).tolist()
    }
    return jsonify(response)


if __name__ == "__main__":
    print("Starting Python Flask Server For FYP - House Price Prediction Web Application")
    util.load_saved_artifacts()
    app.run()
