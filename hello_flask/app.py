import re
from datetime import datetime
from flask import Flask, request
from flask import render_template
import requests

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
        URL = 'https://jsonplaceholder.typicode.com/comments?postId='+language+'&email='+framework
        response = requests.get(URL)
        if response.status_code == 200:
            print('Registro encontrado:')
            print('Data:', response.json())
        else:
            print('Error en la solicitud, detalles:', response.text)
        return '''
            <form action="javascript:window.close();">
                <div><label>Tipo de documento: <input type="text" name="name" readonly></label></div>
                <div><label>Número de documento: <input type="number" name="email" readonly></label></div>
                <input type="submit" value="Cerrar">
                <h4>Tipo de documento: {}</h4>
                <h4>Número de documento: {}</h4>'''.format(language, framework)
    else:
        # otherwise handle the GET request
        return '''
           <form method="POST">
               <div><label>Tipo de documento: <input type="text" name="name"></label></div>
               <div><label>Número de documento: <input type="number" name="email"></label></div>
               <input type="submit" value="Submit">
           </form>'''