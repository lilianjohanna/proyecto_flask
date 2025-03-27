import re
from datetime import datetime
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
@app.route("/hello/<name>")
def hello_there(name='Lilian Johanna'):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )