from flask import Flask, request, Response
from flask import render_template
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("base.html")


@app.route("/upload-file", methods=['GET', 'POST'])
def upload_file():
    print(f"Entered upload\n{request.method}", flush=True)
    if request.method == 'GET':
        return os.getcwd()
    if request.method == 'POST':
        print('Entered post request', flush=True)
        model = request.files['model']
        binary = request.files['binary']
        model.save(os.path.join('./mysite/project/app/static', secure_filename(model.filename)))
        binary.save(os.path.join('./mysite/project/app/static', secure_filename(binary.filename)))
        return Response(status=200)
