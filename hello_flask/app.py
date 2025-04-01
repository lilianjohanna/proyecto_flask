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
        auth_url = 'https://vanti.ecs-la.com/VantiListoServicesNMTest/api/Auth/LoginApi'
        datos={"username":"info@adndigital.co","password":"Vanti2023*"}
        response = requests.post(auth_url,json=datos)
        if response.status_code == 200:
            token=response.json().get("token")
            print("Token obtenido: ", token)
        else:
            print(f"Error al obtener el token: {response.status_code} - {response.text}")
    else:
        # otherwise handle the GET request
        return '''
           <form method="POST">
               <div><label>Tipo de documento: <input type="text" name="name"></label></div>
               <div><label>Número de documento: <input type="text" name="email"></label></div>
               <input type="submit" value="Submit">
           </form>'''