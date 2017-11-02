from Data import Data
from bme590hrm.Processing import Processing
from bme590hrm.Vitals import Vitals
from bme590hrm.Diagnosis import Diagnosis
from flask import Flask, request, jsonify
app = Flask(__name__)
import numpy as np
import json
#    pip install Flask
#    $ FLASK_APP = hello.py flask run


def send_error(message, code):
    """ Sends Errors through Web Service"""
    err = {
        "error": message
    }
    return jsonify(err), code


@app.route("/api/heart_rate/summary")
def summary():
    """ Runs Web Service
    :param: time: user inputted as json dictionary
    :param: voltage: user inputted as json dictionary
    :rtype: json dictionary output of time, instantaneous_heart_rate, tachycardia_annotations, brachycardia_annotations
    """
    j_dict = request.json()
    try:
        json.loads(j_dict)
        # load is for file, loads is for string
    except ValueError:
        return send_error("Input is not JSON dictionary", 600)
    t = np.array(j_dict['time'])
    v = np.array(j_dict['voltage'])
    data_checker = Data(t, v)
    if data_checker.value_range_result() is True & data_checker.value_type_result() is True:
        hr = np.column_stack((t, v))
    peak_data = Processing()
    peak_data.ecg_peakdetect(hr)
    peak_times = peak_data.t
    inst_data = Vitals(peak_times)
    inst_hr_output = inst_data.inst_hr_array
    brachy_output = inst_data.brachy_result
    tachy_output = inst_data.tachy_result
    time_dict = {"time": t.tolist()}
    inst_hr_dict = {"instantaneous_heart_rate": inst_hr_output.tolist()}
    tachy_dict = {"tachycardia_annotations": tachy_output.tolist()}
    brachy_dict = {"brachycardia_annotations": brachy_output.tolist()}
    summary_content = [time_dict, inst_hr_dict, tachy_dict, brachy_dict]
    return jsonify(summary_content)


@app.route("/api/heart_rate/average")
def average():
    """ Runs Web Service
    :param: time: user inputted as json dictionary
    :param: voltage: user inputted as json dictionary
    :param: averaging_period: user inputted as json dictionary
    :rtype: json dictionary output of time_interval, average_heart_rate, tachycardia_annotations, brachycardia_annotations
    """
    j_dict = request.json()
    try:
        json.loads(j_dict)
        # load is for file, loads is for string
    except ValueError:
        return send_error("Input is not JSON dictionary", 600)
    t = np.array(j_dict['time'])
    v = np.array(j_dict['voltage'])
    avg_period = np.array(j_dict['averaging_period'])
    data_checker = Data(t, v)
    if data_checker.value_range_result() is True & data_checker.value_type_result() is True:
        hr = np.column_stack((t, v))
    peak_data = Processing()
    peak_data.ecg_peakdetect(hr)
    peak_times = peak_data.t
    inst_data = Vitals(peak_times)
    avg_hr_output = inst_data.avg_hr_array
    tachy_output = inst_data.tachy_result
    brachy_output = inst_data.brachy_result
    avg_period_dict = {"averaging_period": avg_period.tolist()}
    time_dict = {"time_interval": t.tolist()}
    avg_hr_dict = {"average_heart_rate": avg_hr_output.tolist()}
    tachy_dict = {"tachycardia_annotations": tachy_output.tolist()}
    brachy_dict = {"brachycardia_annotations": brachy_output.tolist()}
    average_content = [avg_period_dict, time_dict, avg_hr_dict, tachy_dict, brachy_dict]
    return jsonify(average_content)

# data = Data(t, v)
# try:
#     data.verify()
# except ValueError as inst:
#     print(inst.message)
#     send_error(efsdgknf + inst.message, 400)
