from Data import Data
from bme590hrm.Processing import Processing
from bme590hrm.Vitals import Vitals
from bme590hrm.Diagnosis import Diagnosis
from flask import Flask, request, jsonify
app = Flask(__name__)
import numpy as np
#    pip install Flask
#    $ FLASK_APP = hello.py flask run

counter = 0

def send_error(message, code):
    """
    Sends errors through our web service
    :param message: error message to be sent
    :param code: HTTP status code
    :rtype: jsonified error code and status code
    """

    err = {
        "error": message
    }
    return jsonify(err), code


# @app.route("/api/heart_rate/summary")
# def summary():
#     """
#     Runs web service
#     :param: time: user inputted as json dictionary
#     :param: voltage: user inputted as json dictionary
#     :rtype: json dictionary output of time, instantaneous_heart_rate, tachycardia_annotations, brachycardia_annotations
#     """
#     global counter
#     j_dict = request.json()
#     try:
#         j_dict.json()
#     except ValueError:
#         return send_error("Input is not JSON dictionary", 400)
#     t = np.array(j_dict['time'])
#     v = np.array(j_dict['voltage'])
#     data = Data(t, v)
#     if data.value_range_result() is True & data.value_type_result() is True:
#         hr = np.column_stack((t, v))
#
#     peak_data = Processing()
#     peak_data.ecg_peakdetect(hr)
#     peak_times = peak_data.t
#
#     hr_data = Vitals(peak_times, hr[:, 0])
#     inst_hr_array = hr_data.inst_hr_array
#     try:
#         inst_hr_diagnosis = Diagnosis(inst_hr_array)
#     except ValueError as inst:
#         print(inst.message)
#         send_error(inst.message, 400)
#
#     brachy_output = inst_hr_diagnosis.brachy_result
#     tachy_output = inst_hr_diagnosis.tachy_result
#
#     time_dict = {"time": t.tolist()}
#     inst_hr_dict = {"instantaneous_heart_rate": inst_hr_output.tolist()}
#     tachy_dict = {"tachycardia_annotations": tachy_output.tolist()}
#     brachy_dict = {"brachycardia_annotations": brachy_output.tolist()}
#     summary_content = [time_dict, inst_hr_dict, tachy_dict, brachy_dict]
#     counter = counter + 1
#     return jsonify(summary_content)
#
#
# @app.route("/api/heart_rate/average")
# def average():
#     """
#     Runs Web Service
#     :param: time: user inputted as json dictionary
#     :param: voltage: user inputted as json dictionary
#     :param: averaging_period: user inputted as json dictionary
#     :rtype: json dictionary output of time_interval, average_heart_rate, tachycardia_annotations, brachycardia_annotations
#     """
#     global counter
#     j_dict = request.json()
#     t = np.array(j_dict['time'])
#     v = np.array(j_dict['voltage'])
#     avg_period = np.array(j_dict['averaging_period'])
#     data = Data(t, v)
#     if data.value_range_result() is True & data.value_type_result() is True:
#         hr = np.column_stack((t, v))
#
#     peak_data = Processing()
#     peak_data.ecg_peakdetect(hr)
#     peak_times = peak_data.t
#
#     hr_data = Vitals(peak_times, hr[:, 0])
#     avg_hr_array = hr_data.avg_hr_array
#     try:
#         avg_hr_diagnosis = Diagnosis(avg_hr_array)
#     except ValueError as inst:
#         print(inst.message)
#         send_error(inst.message, 400)
#     brachy_output = avg_hr_diagnosis.brachy_result
#     tachy_output = avg_hr_diagnosis.tachy_result
#
#     avg_period_dict = {"averaging_period": avg_period.tolist()}
#     time_dict = {"time_interval": t.tolist()}
#     avg_hr_dict = {"average_heart_rate": avg_hr_output.tolist()}
#     tachy_dict = {"tachycardia_annotations": tachy_output.tolist()}
#     brachy_dict = {"brachycardia_annotations": brachy_output.tolist()}
#     average_content = [avg_period_dict, time_dict, avg_hr_dict, tachy_dict, brachy_dict]
#     counter = counter + 1
#     return jsonify(average_content)


@app.route("/api/requests")
def requests():
    """
    return the total number of requests the service has served since its
    most recent reboot.

    :return: counter
    """
    global counter
    counter = counter + 1
    count_json = {"Requests to Date": counter}

    return count_json



# data = Data(t, v)
# try:
#     data.verify()
# except ValueError as inst:
#     print(inst.message)
#     send_error(efsdgknf + inst.message, 400)
