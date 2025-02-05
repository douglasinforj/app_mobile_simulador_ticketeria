import flet as ft
from components.navbar import navbar
from services.api_service import validar_ingresso

def validar_view(page):
    codigo_input = ft.TextField(label="Código do Ingresso")

    def handle_validar(e):
        response = validar_ingresso(codigo_input.value)
        page.snack_bar = ft.SnackBar(ft.Text(response["mensagem"], color="green" if response["status"] else "red"))
        page.snack_bar.open = True
        page.update()

    return ft.View(
        "/validar",
        controls=[
            navbar(page),  # Adicionando a Navbar
            ft.Text("Validar Ingresso", size=20, weight=ft.FontWeight.BOLD),
            codigo_input,
            ft.ElevatedButton("Validar", on_click=handle_validar),
            ft.ElevatedButton("Voltar", on_click=lambda _: page.go("/")),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )
