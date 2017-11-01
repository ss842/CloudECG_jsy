import Data as Import
import flaskapp
import pytest
from flask import Flask, request, jsonify
app = Flask(__name__)


def test_value_type():
    with pytest.raises(TypeError):
        x = Alternative_Data.Data('FaultyData_UnitTest.csv')
        x.value_type()


def test_value_range():
    with pytest.raises(ValueError):
        x = Import.Data('FaultyData_UnitTest.csv')
        x.value_range()


def test_data_is_good():
    good_test_data = Import.Data('GoodData_UnitTest.csv')
    good_test_data.value_type()
    good_test_data.value_range()
    assert good_test_data.value_type_result is True
    assert good_test_data.value_range_result is True


def test_json():
    with pytest.raises(ValueError):
        x = flaskapp.Cloud()
        x.summary()

    #assert type(json_data) == str
    # test = request.get_json['json_data']
    # time_dict = {"time": t.tolist()}
    # return jsonify(time_dict)


# @app.route("/api/test_json_input")
# def test_json_input():
#     json_true =