from flask import Flask, request, jsonify
app = Flask (__name__)

#    pip install Flask
#    $ FLASK_APP = hello.py flask run

@app.route("/api/heart_rate/summary")
def receive():
    dict = request.get_json()  # in a json dict
    #  convert to array for processing
    t = dict['time']
    v = dict['voltage']
    # t and v's are arrays


@app.route("/api/heart_rate/average")
def receiveagain():
    dict = request.get_json()
    #  convert to array for processing
    t = dict['time']
    v = dict['voltage']
    t_avg = dict['averaging_period'] #  in seconds
    # t and v's are arrays


# @app.route("/st_hello", methods=['POST'])
# def structured_hello():
#     print(request.json)
#     return "done %d" % request.json['a']