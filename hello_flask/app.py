import re
from datetime import datetime
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
@app.route("/hello/<name>",methods=["GET", "POST"])
def hello_there(name='Lilian Johanna'):
    return render_template(
        "signup_form.html",
        name=name,
        date=datetime.now()
    )