import flet as ft
from components.navbar import navbar  # Importando a Navbar

def home_view(page):
    return ft.View(
        "/",
        controls=[
            #navbar(page),  # Adicionando a Navbar
            ft.Text("Bem-vindo à Ticket App 🎟️", size=24, weight=ft.FontWeight.BOLD),
            ft.ElevatedButton("Comprar Ingresso", on_click=lambda _: page.go("/comprar")),
            ft.ElevatedButton("Validar Ingresso", on_click=lambda _: page.go("/validar")),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )