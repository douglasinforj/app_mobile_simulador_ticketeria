import flet as ft
from components.navbar import navbar
from services.api_service import comprar_ingresso, buscar_eventos

def comprar_view(page):
    nome_input = ft.TextField(label="Nome")
    cpf_input = ft.TextField(label="CPF")
    evento_input = ft.Dropdown(label="Selecione o Evento")

    # Função para buscar os eventos da API
    def buscar_eventos_na_api():
        eventos = buscar_eventos()
        if eventos:
            evento_input.items = [ft.DropdownOption(label=evento["nome"], value=evento["id"]) for evento in eventos]
        else:
            page.add(ft.Text("Erro ao carregar eventos", color="red"))

    # Chama a função para carregar eventos ao iniciar a tela
    buscar_eventos_na_api()

    def handle_comprar(e):
        nome = nome_input.value
        cpf = cpf_input.value
        evento_id = evento_input.value
        if nome and cpf and evento_id:
            response = comprar_ingresso(nome, cpf, evento_id)
            page.snack_bar = ft.SnackBar(ft.Text(response["mensagem"], color="green" if response["status"] else "red"))
            page.snack_bar.open = True
            page.update()

            if response["status"]:
                # Após a compra, redireciona para a tela com o ingresso
                page.go("/ingresso")
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos corretamente!", color="red"))
            page.snack_bar.open = True
            page.update()

    return ft.View(
        "/comprar",
        controls=[
            navbar(page),  # Adicionando a Navbar
            ft.Text("Comprar Ingresso", size=20, weight=ft.FontWeight.BOLD),
            nome_input,
            cpf_input,
            evento_input,
            ft.ElevatedButton("Comprar", on_click=handle_comprar),
            ft.ElevatedButton("Voltar", on_click=lambda _: page.go("/")),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )
