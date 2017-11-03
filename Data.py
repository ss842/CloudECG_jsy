#  CloudECG_jsy
import numpy as np

#    pip install Flask
#    $ FLASK_APP = hello.py flask run


class Data:

    def __init__(self, time, voltage):
        self.value_range_result = None
        self.data_type_result = None
        self.t = time
        self.v = voltage
        self.value_range()
        self.value_type()

    def value_range(self):
        for x in range(len(self.v)):
            if x >= 300:
                print("Your voltage values seem too high!")
                self.value_range_result = False
                raise ValueError
            else:
                self.value_range_result = True

    def value_type(self):
        for x in range(len(self.v)):
            if x == str:
                print("Your data contains strings!")
                self.data_type_result = False
                raise ValueError
        else:
            self.data_type_result = True
