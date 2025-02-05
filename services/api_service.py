import requests

API_URL = "http://localhost:8000/api/"

def comprar_ingresso(nome, cpf, evento_id):
    try:
        response = requests.post(f"{API_URL}ingressos/", json={"nome": nome, "cpf": cpf, "evento_id": evento_id})
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
        return {"status": False, "mensagem": "Ingresso inválido!"}
    except Exception as e:
        return {"status": False, "mensagem": str(e)}

# Função para buscar eventos da API
def buscar_eventos():
    try:
        response = requests.get(f"{API_URL}eventos/")
        if response.status_code == 200:
            return response.json()  # Retorna a lista de eventos
        return []
    except Exception as e:
        return {"status": False, "mensagem": str(e)}
    

# Busca por cpf
def buscar_nome_por_cpf(cpf):
    try:
        response = requests.get(f"{API_URL}clientes/{cpf}/")
        if response.status_code == 200:
            cliente = response.json()
            return cliente["nome"]
        return None
    except Exception as e:
        return None
    

#função cadastro de cliente:

def cadastrar_cliente(nome, cpf, email, telefone):
    try:
        response = requests.post(f"{API_URL}clientes/", json={
            "nome": nome,
            "cpf": cpf,
            "email": email,
            "telefone": telefone
        })
        if response.status_code == 201:
            return {"status": True, "mensagem": "Cliente cadastrado com sucesso!"}
        return {"status": False, "mensagem": "Erro ao cadastrar cliente!"}
    except Exception as e:
        return {"status": False, "mensagem": str(e)}
