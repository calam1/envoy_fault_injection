from flask import Flask
from flask import send_from_directory 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {
       "message": "Hello"
    }

@app.route("/static/<path:name>")
def download_file(name):
    return send_from_directory(
        'static', name, as_attachment=True
    )