#  CloudECG_jsy

import numpy as np


class Data:

    def __init__(self):
        self.value_range_result = None
        self.data_type_result = None


@app.route("/api/heart_rate/summary")
def receive_summary():
    j_dict = request.get_json()  # in a json dict
    #  convert to array for processing
    t = j_dict['time']
    v = j_dict['voltage']
    # t and v's are arrays for analysis


@app.route("/api/heart_rate/average")
def receive_average():
    j_dict = request.get_json()
    t = j_dict['time']
    v = j_dict['voltage']
    t_avg = j_dict['averaging_period']  # in seconds


def value_range(self):
    for x in range(len(v)):
        if x >= 300:
            print("Your voltage values seem too high!")
            self.value_range_result = False
            raise ValueError
        else:
            self.value_range_result = True


def value_type(self):
    for x in range(0, len(v)):
        if x == str:
            print("Your data contains strings!")
            self.data_type_result = False
            raise ValueError
    else:
        self.data_type_result = True


self.hr = [t, v]


@app.route("/api/heart_rate/summary")
def give_summary():
    # output JSON time, instantaneous_heart_rate, tachycardia_annotations, brachycardia_annotations
    time = jsonify(t)
    instantaneous_heart_rate = jsonify(Vitals.inst_hr_array)
    tachycardia_annotations = jsonify(Diagnosis.tachy_result)
    brachycardia_annotations = jsonify(Diagnosis.brachy_result)
    print(time)
    print(instantaneous_heart_rate)
    print(tachycardia_annotations)
    print(brachycardia_annotations)


@app.route("/api/heart_rate/average")
def give_average():
    # output JSON averaging_period, time_interval, instantaneous_heart_rate, tachycardia_annotations,
    # brachycardia_annotations
    # averaging period = averaging_period
    time_interval = time
    instantaneous_heart_rate = jsonify(Vitals.inst_hr_array)
    tachycardia_annotations = jsonify(Diagnosis.tachy_result)
    brachycardia_annotations = jsonify(Diagnosis.brachy_result)
    print(averaging_period)
    print(time_interval)
    print(instantaneous_heart_rate)
    print(tachycardia_annotations)
    print(brachycardia_annotations)