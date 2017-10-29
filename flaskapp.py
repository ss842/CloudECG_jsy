from flask import Flask, request, jsonify
app = Flask(__name__)

#    pip install Flask
#    $ FLASK_APP = hello.py flask run


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
    #  convert to array for processing
    t = j_dict['time']
    v = j_dict['voltage']
    t_avg = dict['averaging_period']  # in seconds
    # t, v, and t_avg are arrays for analysis


"""
send arrays to Data, Processing, Vitals, Diagnosis classes before return arrray's 
"""

@app.route("/api/heart_rate/summary")
def give_summary():
    # output JSON time, instantaneous_heart_rate, tachycardia_annotations, brachycardia_annotations
    # time =
    # instantaneous_heart_rate =
    # tachycardia_annotations =
    # brachycardia_annotations =


# @app.route("/st_hello", methods=['POST'])
# def structured_hello():
#     print(request.json)
#     return "done %d" % request.json['a']
