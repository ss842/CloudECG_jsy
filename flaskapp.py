import Data
from flask import Flask, request, jsonify
app = Flask(__name__)

#    pip install Flask
#    $ FLASK_APP = hello.py flask run


@app.route("/api/heart_rate/summary")
def summary():
    j_dict = request.get_json()  # in a json dict
    #  convert to array for processing
    t = j_dict['time']
    v = j_dict['voltage']
    data_checker = Data(t, v)
    if data_checker.value_range_result is True & data_checker.value_type_result is True:
        self.hr = [t, v]


    # Data.value_range(request.get_json())
    # Data.value_type(request.get_json())

@app.route("/api/heart_rate/average")
def average():
    j_dict = request.get_json()
    #  convert to array for processing
    t = j_dict['time']
    v = j_dict['voltage']
    t_avg = dict['averaging_period']  # in seconds
    # t, v, and t_avg are arrays for analysis


# @app.route("/api/heart_rate/summary")
# def give_summary():
#     # output JSON time, instantaneous_heart_rate, tachycardia_annotations, brachycardia_annotations
#     time = jsonify(t)
#     instantaneous_heart_rate = jsonify(Vitals.inst_hr_array)
#     tachycardia_annotations = jsonify(Diagnosis.tachy_result)
#     brachycardia_annotations = jsonify(Diagnosis.brachy_result)
#     return time
#     return instantaneous_heart_rate
#     return (tachycardia_annotations
#     return (brachycardia_annotations


# @app.route("/api/heart_rate/average")
# def give_average():
#     # output JSON averaging_period, time_interval, instantaneous_heart_rate, tachycardia_annotations,
#     # brachycardia_annotations
#     # averaging period = averaging_period
#     time_interval = time
#     instantaneous_heart_rate = jsonify(Vitals.inst_hr_array)
#     tachycardia_annotations = jsonify(Diagnosis.tachy_result)
#     brachycardia_annotations = jsonify(Diagnosis.brachy_result)
#     print(averaging_period)
#     print(time_interval)
#     print(instantaneous_heart_rate)
#     print(tachycardia_annotations)
#     print(brachycardia_annotations)


# @app.route("/api/heart_rate/summary")
# def give_summary():
#     # output JSON time, instantaneous_heart_rate, tachycardia_annotations, brachycardia_annotations
#     # time =
#     # instantaneous_heart_rate =
#     # tachycardia_annotations =
#     # brachycardia_annotations =


# @app.route("/st_hello", methods=['POST'])
# def structured_hello():
#     print(request.json)
#     return "done %d" % request.json['a']
