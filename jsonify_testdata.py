from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)
filename = 'test_data/test_data1.csv'
@app.route("/data")
def csv_to_json(filename):
    filename_array = np.genfromtxt(filename,delimiter=','
                                   , missing_values='', filling_values=0.0)
    time_array = filename_array[:, 0]
    v_array = filename_array[:, 1]
    time = {"time": time_array.tolist()}
    voltage = {"voltage": v_array.tolist()}
    arr = [time, voltage]
    return jsonify(arr)

# @app.route("/st_hello", methods=['POST'])
# def structured_hello():
#     print(request.json)
#     return "Done %d" % request.json['a']
