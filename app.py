import urllib.request

import flask
from flask import Flask, render_template, Response

app = Flask(__name__)


@app.route('/')
def output():
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    resp = flask.Response(urllib.request.urlopen(url))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'application/json'
    resp.headers['X-Content-Type-Options'] = 'nosniff'
    return resp


if __name__ == "__main__":
    app.run()
