import flet as ft
from components.navbar import navbar
from services.api_service import cadastrar_cliente

def cadastro_view(page):
    # Campos de entrada para cadastro
    nome_input = ft.TextField(label="Nome", autofocus=True)
    cpf_input = ft.TextField(label="CPF")
    email_input = ft.TextField(label="Email")
    telefone_input = ft.TextField(label="Telefone")

    def handle_cadastrar(e):
        # Pegando os dados inseridos pelo usuário
        nome = nome_input.value
        cpf = cpf_input.value
        email = email_input.value
        telefone = telefone_input.value

        # Verificando se os campos estão preenchidos
        if nome and cpf and email and telefone:
            response = cadastrar_cliente(nome, cpf, email, telefone)
            page.snack_bar = ft.SnackBar(ft.Text(response["mensagem"], color="green" if response["status"] else "red"))
            page.snack_bar.open = True
            page.update()

            if response["status"]:
                # Limpar os campos após o cadastro
                nome_input.value = ""
                cpf_input.value = ""
                email_input.value = ""
                telefone_input.value = ""
                page.update()

                # Após o cadastro, redireciona para a tela inicial
                page.go("/")
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos corretamente!", color="red"))
            page.snack_bar.open = True
            page.update()

    return ft.View(
        "/cadastro",
        controls=[
            navbar(page),  # Adicionando a Navbar
            ft.Text("Cadastro de Cliente", size=20, weight=ft.FontWeight.BOLD),
            nome_input,
            cpf_input,
            email_input,
            telefone_input,
            ft.ElevatedButton("Cadastrar", on_click=handle_cadastrar),
            ft.ElevatedButton("Voltar", on_click=lambda _: page.go("/")),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )
