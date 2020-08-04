import flask
import os
import socket

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return flask.jsonify({"pod_name": socket.getfqdn(), "pod_ips": socket.gethostbyname_ex(socket.getfqdn())[-1]})

@app.route('/identity', methods=['GET'])
def identity():
    return flask.jsonify({"headers": {k:v for k, v in flask.request.headers.items()}})

@app.route('/server', methods=['GET'])
def server():
    return flask.jsonify({"environment": {k:v for k, v in os.environ.items()}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
