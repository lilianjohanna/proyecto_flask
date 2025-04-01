import requests
def hello_there():
    auth_url = 'https://vanti.ecs-la.com/VantiListoServicesNMTest/api/Auth/LoginApi'
    datos={"username":"info@adndigital.co","password":"Vanti2023*"}
    response = requests.post(auth_url,json=datos)
    if response.status_code == 200:
        token=response.json().get("token")
        print("Token obtenido: ", token)
    else:
        print(f"Error al obtener el token: {response.status_code} - {response.text}")