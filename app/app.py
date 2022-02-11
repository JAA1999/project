from flask import Flask, request
from flask import render_template
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Text"
    return render_template("base.html")


@app.route("/update_model", methods=['POST'])
def update_model():
    model_file = request._get_file_stream()
    with open("app/static/model.gltf", 'rb') as f:
        f.write(model_file.read())
    return "", 204
