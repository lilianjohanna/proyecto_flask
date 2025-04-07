import re
from datetime import datetime
from flask import Flask, request, jsonify, render_template
import requests
import json
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
jwt = JWTManager(app)

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
@app.route("/hello/<name>", methods=['GET', 'POST'])
def hello_there():
    # handle the POST request
    if request.method == 'POST':
        language = request.form.get('name')
        framework = request.form.get('email')
        URL = 'https://www.datos.gov.co/resource/6cat-2gcs.json?nit='+language+'&supervisor='+framework
        response = requests.get(URL)
        if response.status_code == 200:
            #print('Registro encontrado:')
            #print('Data:', response.json())
            listaresultados=json.dumps(response.json())
            totallista=len(listaresultados)
            resultadofinal=[]
            for items in item2:
                resultadofinal.append(items)
                item2=resultadofinal
            return '''
                <form action="javascript:window.close();">
                    <div><label>NIT: <input type="text" name="name" readonly></label></div>
                    <div><label>Supervisor: <input type="text" name="email" readonly></label></div>
                    <input type="submit" value="Cerrar">
                    <h4>Tipo de documento: {}</h4>
                    <h4>Número de documento: {}</h4>'''.format(language, framework)+item2
        else:
            #print('Error en la solicitud, detalles:', response.text)
            return '''
                <form action="javascript:window.close();">
                    <div><label>NIT: <input type="text" name="name" readonly></label></div>
                    <div><label>Supervisor: <input type="text" name="email" readonly></label></div>
                    <input type="submit" value="Cerrar">
                    <h4>Tipo de documento: {}</h4>
                    <h4>Número de documento: {}</h4>'''.format(language, framework)+json.dumps(response.text)
    else:
        # otherwise handle the GET request
        return '''
           <form method="POST">
               <div><label>NIT: <input type="text" name="name"></label></div>
               <div><label>Supervisor: <input type="text" name="email"></label></div>
               <input type="submit" value="Submit">
           </form>'''