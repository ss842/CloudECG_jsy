from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route("/api/heart_rate/summary", methods=['POST'])
def hello():
    time = {"time": [0, 1, 2, 3, 4]}
    voltage = {"voltage": [30, 40, 50, 60]}
    arr = [time, voltage]
    return jsonify(arr)

@app.route("/api/heart_rate/summary")
def trial_get():
    t = request.args.get('time')
    #t = j_dict['time']
    #v = j_dict['voltage']

    #hr = [t, v]
    return t

# @app.route("/api/heart_rate/summary", methods=['GET'])
# def trial_get():
#     j_dict = request.get_json()
#     t = j_dict['time']
#     v = j_dict['voltage']
#
#     hr = [t, v]
#     return hr
#
#
# test = trial_get()
#
# print(test)
