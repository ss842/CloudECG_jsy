#  CloudECG_jsy

import numpy as np


class Data:

    def __init__(self, filename='ecg_testdata.csv'):
        self.value_range_result = None
        self.data_type_result = None


@app.route("/api/heart_rate/summary")
def receive_summary():
    j_dict = request.get_json()  # in a json dict
    #  convert to array for processing
    t = j_dict['time']
    v = j_dict['voltage']
    # t and v's are arrays for analysis


def value_range(self):
    for x in range(len(v)):
        if x >= 300:
            print("Your voltage values seem too high!")
            self.value_range_result = False
            raise ValueError
        else:
            self.value_range_result = True


def data_type(self):
    for x in range(0, len(v)):
        if x == str:
            print("Your data contains strings!")
            self.data_type_result = False
            raise ValueError
    else:
        self.data_type_result = True


self.hr = [t, v]


@app.route("/api/heart_rate/average")
def receive_average():
    j_dict = request.get_json()
    t = j_dict['time']
    v = j_dict['voltage']
    t_avg = j_dict['averaging_period']  # in seconds

    for row in range(len(self.filename_array)):
        if self.filename_array[row, 1] >= 300:
            print("Your voltage values seem too high!")
            self.value_range_result = False
            raise ValueError
        else:
            self.value_range_result = True




