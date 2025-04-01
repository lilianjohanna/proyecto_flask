import re
from datetime import datetime
from flask import Flask, request, jsonify, render_template
import requests
import json
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
jwt = JWTManager(app)

app = Flask(__name__)

def hello_there():
    auth_url = 'https://vanti.ecs-la.com/VantiListoServicesNMTest/api/Auth/LoginApi'
    datos={"username":"info@adndigital.co","password":"Vanti2023*"}
    response = requests.post(auth_url,json=datos)
    if response.status_code == 200:
        token=response.json().get("token")
        print("Token obtenido: ", token)
    else:
        print(f"Error al obtener el token: {response.status_code} - {response.text}")