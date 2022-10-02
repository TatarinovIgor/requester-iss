import urllib.request
from flask import Flask, render_template

app = Flask(__name__, )


@app.route('/')
def output():
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    return response


if __name__ == "__main__":
    app.run()
