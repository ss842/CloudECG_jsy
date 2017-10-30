import Data as D
import Processing as P
import Vitals as V
import Diagnosis as Dia
from flask import Flask, request, jsonify
app = Flask(__name__)

#    pip install Flask
#    $ FLASK_APP = hello.py flask run


class Cloud:

    def __init__(self):
        self.cloud_count = 0

    @app.route("/api/heart_rate/summary")
    def summary(self):
        j_dict = request.get_json()  # in a json dict
        #  convert to array for processing
        t = j_dict['time']
        v = j_dict['voltage']
        data_checker = D.Data(t, v)
        if data_checker.value_range_result is True & data_checker.value_type_result is True:
            hr = [t, v]
        peak_data = P.Processing()
        peak_data.ecg_peakdetect(hr)
        peak_times = peak_data.t
        inst_data = V.Vitals(peak_times)
        inst_hr_output = inst_data.inst_hr_array
        tachy_output = inst_data.tachy_result
        brachy_output = inst_data.brachy_result
        #  output JSON time, instantaneous_heart_rate, tachycardia_annotations, brachycardia_annotations
        time_dict = {"time": t.tolist()}
        inst_hr_dict = {"instantaneous_heart_rate": inst_hr_output.tolist()}
        tachy_dict = {"tachycardia_annotations": tachy_output.tolist()}
        brachy_dict = {"brachycardia_annotations": brachy_output.tolist()}
        summary_content = [time_dict, inst_hr_dict, tachy_dict, brachy_dict]
        return jsonify(summary_content)

    @app.route("/api/heart_rate/average")
    def average(self):
        j_dict = request.get_json()  # in a json dict
        #  convert to array for processing
        t = j_dict['time']
        v = j_dict['voltage']
        avg_period = j_dict['averaging_period']
        data_checker = D.Data(t, v)
        if data_checker.value_range_result is True & data_checker.value_type_result is True:
            hr = [t, v]
        peak_data = P.Processing()
        peak_data.ecg_peakdetect(hr)
        peak_times = peak_data.t
        inst_data = V.Vitals(peak_times)
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
