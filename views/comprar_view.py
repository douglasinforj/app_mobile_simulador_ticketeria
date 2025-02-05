import flet as ft
from components.navbar import navbar
from services.api_service import comprar_ingresso, buscar_eventos, buscar_nome_por_cpf

import asyncio





# Função para buscar os eventos da API
def comprar_view(page):
    cpf_input = ft.TextField(label="CPF")
    nome_input = ft.TextField(label="Nome", disabled=True)  # Desabilitar o campo de nome, pois será preenchido automaticamente.
    evento_input = ft.Dropdown(label="Selecione o Evento")

    # Função para buscar os eventos da API
    def buscar_eventos_na_api():
        eventos = buscar_eventos()  # Supondo que essa função faça uma chamada à API para buscar os eventos
        print(eventos)             # Verifique no console se os dados dos eventos estão chegando corretamente

        #TODO:teste recebimento de dados
        #print(eventos)  # Verifique no console se os dados dos eventos estão chegando corretamente
        if eventos:
            # Atualiza os itens do Dropdown com a lista de eventos
            evento_input.options = [
            ft.dropdown.Option(key=str(evento["id"]), text=evento["nome"]) 
            for evento in eventos
            ]
            
            # Certifique-se de que o Dropdown foi adicionado à página
            if evento_input not in page.controls:
                page.add(evento_input)  # Adiciona o Dropdown à página, se ainda não estiver
                page.update()  # Atualiza a página após adicionar o controle

            evento_input.update()  # Atualiza apenas o componente dropdown
        else:
            # Caso não haja eventos, exibe uma mensagem de erro
            page.add(ft.Text("Erro ao carregar eventos", color="red"))
            page.update()  # Atualiza a página para exibir a mensagem de erro





    # Função para buscar o nome do usuário pelo CPF
    def buscar_nome_por_cpf_input(cpf):
        nome = buscar_nome_por_cpf(cpf)
        if nome:
            nome_input.value = nome
        else:
            nome_input.value = ""  # Limpa o campo se o CPF não for encontrado
            page.snack_bar = ft.SnackBar(ft.Text("CPF não encontrado!", color="red"))
            page.snack_bar.open = True
        page.update()

    # Função chamada ao alterar o CPF no campo de texto
    def on_cpf_change(e):
        cpf = cpf_input.value.strip()
        if cpf:
            buscar_nome_por_cpf_input(cpf)  # Busca o nome e atualiza automaticamente
        else:
            nome_input.value = ""  # Limpa o campo se o CPF for apagado
            page.update()

    # Chama a função para carregar eventos ao iniciar a tela
    buscar_eventos_na_api()

    # Atualiza o nome automaticamente ao alterar o CPF
    cpf_input.on_change = on_cpf_change



    def handle_comprar(e):
        cpf = cpf_input.value
        evento_id = evento_input.value
        
        if cpf and evento_id:
            response = comprar_ingresso(nome_input.value, cpf, evento_id)  # Envia o nome automaticamente
            
            if response["status"]:
                codigo_ingresso = response["codigo_ingresso"]  # Extrai o código do ingresso
                page.snack_bar = ft.SnackBar(ft.Text(response["mensagem"], color="green"))
                page.snack_bar.open = True
                page.update()
                
                # Redirecionar para a tela do ingresso com o código na URL
                page.go(f"/ingresso/{codigo_ingresso}")
            else:
                page.snack_bar = ft.SnackBar(ft.Text(response["mensagem"], color="red"))
                page.snack_bar.open = True
                page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos corretamente!", color="red"))
            page.snack_bar.open = True
            page.update()

    return ft.View(
        "/comprar",
        controls=[
            navbar(page),  # Adicionando a Navbar
            ft.Text("Comprar Ingresso", size=20, weight=ft.FontWeight.BOLD),
            cpf_input,
            #nome_input,  # Nome será preenchido automaticamente
            evento_input,
            ft.ElevatedButton("Comprar", on_click=handle_comprar),
            ft.ElevatedButton("Voltar", on_click=lambda _: page.go("/")),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )
