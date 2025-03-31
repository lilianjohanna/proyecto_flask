import re
from datetime import datetime
from flask import Flask, request
from flask import render_template

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
@app.route("/hello/<name>", methods=['GET', 'POST'])
#def hello_there(name='Lilian Johanna'):
    #return render_template(
        #"signup_form.html",
        #name=name,
        #date=datetime.now()
    #)
def hello_there():
    # handle the POST request
    if request.method == 'POST':
        language = request.form.get('name')
        framework = request.form.get('email')
        return '''
                  <h1>The name value is: {}</h1>
                  <h1>The email value is: {}</h1>'''.format(language, framework)
    else:
        # otherwise handle the GET request
        return '''
           <form method="POST">
               <div><label>Language: <input type="text" name="name"></label></div>
               <div><label>Framework: <input type="text" name="email"></label></div>
               <input type="submit" value="Submit">
           </form>'''