import flet as ft 

def navbar(page):
    return ft.Row([
        ft.ElevatedButton("Início", on_click=lambda _: page.go("/")),
        ft.ElevatedButton("Comprar", on_click=lambda _: page.go("/comprar")),
        ft.ElevatedButton("Validar", on_click=lambda _: page.go("/validar")),
    ])