from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, world!</p>"

@app.route("/deda")
def hello_deda():
    return "<p>Hello, stariy!</p>"