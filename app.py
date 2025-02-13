
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route("/string")
#returning string
def string_response():
    return "Hello from <b> flask-basic-app! </b>"

@app.route("/json")
#returning JSON using jsonify
def json_response():
    #return {"message": "Hello JSON!"}
    return jsonify(message="Hello jsonify!")
