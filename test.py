import data
import json as js


from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST'])
def hello_world():
    json = request.json
    input_data = data.creatingData(json["name"], json["product"], json["category"], json["price"])
    
    return str(input_data)