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
            if self.v[x] >= 300:
                print("Your voltage values seem too high!")
                self.value_range_result = False
                raise ValueError
            else:
                self.value_range_result = True

    def value_type(self):
        for x in range(len(self.v)):
            try:
                float(self.v[x])
                self.data_type_result = True
            except(TypeError, ValueError):
                print("Your data contains strings!")
                self.data_type_result = False
                raise ValueError
