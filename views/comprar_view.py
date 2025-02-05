import flet as ft
from components.navbar import navbar
from services.api_service import comprar_ingresso, buscar_eventos, buscar_nome_por_cpf

def comprar_view(page):
    cpf_input = ft.TextField(label="CPF")
    nome_input = ft.TextField(label="Nome", enabled=False)  # Desabilitar o campo de nome, pois será preenchido automaticamente.
    evento_input = ft.Dropdown(label="Selecione o Evento")

    # Função para buscar os eventos da API
    def buscar_eventos_na_api():
        eventos = buscar_eventos()
        if eventos:
            evento_input.items = [ft.DropdownOption(label=evento["nome"], value=evento["id"]) for evento in eventos]
        else:
            page.add(ft.Text("Erro ao carregar eventos", color="red"))

    # Função para buscar o nome do usuário pelo CPF
    def buscar_nome_por_cpf_input(cpf):
        nome = buscar_nome_por_cpf(cpf)
        if nome:
            nome_input.value = nome
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("CPF não encontrado!", color="red"))
            page.snack_bar.open = True
            page.update()

    # Função chamada ao alterar o CPF no campo de texto
    def on_cpf_change(e):
        if cpf_input.value:
            buscar_nome_por_cpf_input(cpf_input.value)
        else:
            nome_input.value = ""  # Limpa o campo de nome se o CPF for apagado
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
            cpf_input,
            nome_input,  # Nome será preenchido automaticamente
            evento_input,
            ft.ElevatedButton("Comprar", on_click=handle_comprar),
            ft.ElevatedButton("Voltar", on_click=lambda _: page.go("/")),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )
