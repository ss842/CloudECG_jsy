from flask import Flask, request, jsonify
import sys
app = Flask(__name__)

print(sys.path)

# @app.route("/api/heart_rate/summary/", methods=['POST'])
# def trial_get():
#     print(request.json)
#     return "done"

@app.route("/api/heart_rate/summary", methods=['POST'])
def trial_get():
    data = request.json
    t = data['time']
    #t = j_dict['time']
    #v = j_dict['voltage']

    #hr = [t, v]
    return jsonify(t)