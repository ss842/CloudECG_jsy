from flask import Flask, request, jsonify
app = Flask(__name__)


# @app.route("/api/heart_rate/summary")
# def hello():
#     time = {"time": [0, 1, 2, 3, 4]}
#     voltage = {"voltage": [30, 40, 50, 60]}
#     arr = [time, voltage]
#     return jsonify(arr)

@app.route("/api/heart_rate/summary/", methods=['POST'])
def trial_get():
    data = request.get_json(force=True, silent=False, cache=True)
    t = data['time']
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
