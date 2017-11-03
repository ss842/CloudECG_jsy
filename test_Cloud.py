# import Data as Import
# import Cloud
import pytest
import json
import numpy as np

#app = Flask(__name__)

def test_json_input():
    python_list = [1, 2, 3]
    json_input = json.dumps({"array": [1,2,3]})

    python_object = json.loads(json_input)

    assert python_list == python_object['array']


def test_sec_conversion():
    SEC_TO_MIN = 60

    python_avg_period = np.array([.25])

    json_input = json.dumps({"averaging_period": [15]})
    json_input = json.loads(json_input)
    print(json_input)
    print(type(json_input))
    json_input_value = np.array(json_input['averaging_period'])/SEC_TO_MIN

    assert json_input_value == python_avg_period


    #
    # python_object = json.loads(json_input)
    #
    # #
    # # json_r = json.dumps({"array": 15})
    # #
    # # python_json_r = json.loads(json_r)
    #
    # python_json_r = json.JSONDecoder().decode({"array": 15})
    #
    # v_array = np.array(python_json_r['array'])
    #
    # v_array = v_array / SEC_TO_MIN
    #
    # assert v_array == avg_period_in_minutes
