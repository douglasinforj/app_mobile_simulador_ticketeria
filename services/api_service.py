import requests

API_URL = "http://localhost:8000/api/"

def comprar_ingresso(nome, cpf):
    try:
        response = requests.post(f"{API_URL}ingressos/", json={"nome": nome, "cpf":cpf})
        if response.status_code == 201:
            ingresso = response.json()
            return {"status": True, "mensagem": f"Ingresso Comprado! Código:{ingresso['codigo_ingresso']}"}
        return {"status": False, "mensagem": "Erro ao comprar ingresso!"}
    except Exception as e:
        return {"status": False, "mensagem": str(e)}

def validar_ingresso(codigo):
    try:
        response = requests.get(f"{API_URL}validar-ingresso/{codigo}/")
        if response.status_code == 200:
            return {"status": True, "mensagem": "Ingresso válido!"}
        return {"status": False, "mensagem":"Ingresso inválido!"}
    except Exception as e:
        return {"status": False, "mensagem": str(e)}