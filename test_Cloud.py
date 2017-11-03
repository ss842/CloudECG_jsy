# import Data as Import
# import Cloud
import pytest
import json
import flask
import numpy as np

#app = Flask(__name__)

def test_json_input():

    r = {"array": [1,2,3]}
    json_r = json.dumps({"array": [1,2,3]})

    python_json_r = json.loads(json_r)

    assert python_json_r == r


def test_sec_conversion():
    SEC_TO_MIN = 60
    avg_period_in_minutes = .25

    r = {"array": 15}


    #
    # json_r = json.dumps({"array": 15})
    #
    # python_json_r = json.loads(json_r)

    python_json_r = json.JSONDecoder().decode(r)

    v_array = np.array(python_json_r['array'])

    v_array = v_array / SEC_TO_MIN

    assert v_array == avg_period_in_minutes
