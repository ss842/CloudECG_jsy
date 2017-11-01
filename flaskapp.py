from Data import Data
from Processing import Processing
from Vitals import Vitals
from Diagnosis import Diagnosis
from flask import Flask, request, jsonify
app = Flask(__name__)
#    pip install Flask
#    $ FLASK_APP = hello.py flask run


def send_error(message, code):
    err = {
        "error": message
    }
    return jsonify(err), code


def create_array(t, v):
    data_checker = Data(t, v)
    # make inst of Data, need to fill in !!
    if data_checker.value_range_result is True & data_checker.value_type_result is True:
        hr = [t, v]
    peak_data = Processing()
    peak_data.ecg_peakdetect(hr)
    peak_times = peak_data.t


def get_brachy_tachy(peak_times):
    inst_data = Vitals(peak_times)
    inst_hr_output = inst_data.inst_hr_array
    tachy_output = inst_data.tachy_result
    brachy_output = inst_data.brachy_result
    inst_hr_dict = {"instantaneous_heart_rate": inst_hr_output.tolist()}
    tachy_dict = {"tachycardia_annotations": tachy_output.tolist()}
    brachy_dict = {"brachycardia_annotations": brachy_output.tolist()}


@app.route("/api/heart_rate/summary")
def summary():
    j_dict = request.get_json()
    try:
        j_dict.json()
    except ValueError:
        return send_error("Input is not JSON dictionary", 400)
    #  convert to array for processing
    t = j_dict['time']
    v = j_dict['voltage']
    #  output JSON time, instantaneous_heart_rate, tachycardia_annotations, brachycardia_annotations
    # time_dict = {"time": t.tolist()}
    # inst_data = create_array(t,v)
    # inst_result = get_brachy_tachy(inst_hr_dict, tach_dict, brachy_dict)
    # summary_content = (inst_data) (inst_result)
    # summary_content = [time_dict, inst_hr_dict, tachy_dict, brachy_dict]
    return jsonify(summary_content)


@app.route("/api/heart_rate/average")
def average():
    j_dict = request.get_json()  # in a json dict
    #  convert to array for processing
    t = j_dict['time']
    v = j_dict['voltage']
    avg_period = j_dict['averaging_period']
    data_checker = Data(t, v)
    if data_checker.value_range_result is True & data_checker.value_type_result is True:
        hr = [t, v]
    peak_data = Processing()
    peak_data.ecg_peakdetect(hr)
    peak_times = peak_data.t
    inst_data = Vitals(peak_times)
    # avg_hr_output =
    tachy_output = inst_data.tachy_result
    brachy_output = inst_data.brachy_result
    #  output JSON time, instantaneous_heart_rate, tachycardia_annotations, brachycardia_annotations
    avg_period_dict = {"averaging_period": avg_period.tolist()}
    time_dict = {"time_interval": t.tolist()}
    avg_hr_dict = {"average_heart_rate": avg_hr_output.tolist()}
    tachy_dict = {"tachycardia_annotations": tachy_output.tolist()}
    brachy_dict = {"brachycardia_annotations": brachy_output.tolist()}
    average_content = [avg_period_dict, time_dict, avg_hr_dict, tachy_dict, brachy_dict]
    return jsonify(average_content)

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

# Data.value_range(request.get_json())
# Data.value_type(request.get_json())


    # data = Data(t, v)
    # try:
    #     data.verify()
    # except ValueError as inst:
    #     print(inst.message)
    #     send_error(efsdgknf + inst.message, 400)