import flet as ft
from views.home_view import home_view
from views.comprar_view import comprar_view
from views.validar_view import validar_view
from views.ingresso_view import ingresso_view  # Importando a nova view de ingresso
from views.cadastro_view import cadastro_view 

def main(page: ft.Page):
    page.title = "Ticket App 🎟️"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Criar as views uma única vez
    views = {
        "/": home_view(page),
        "/comprar": comprar_view(page),
        "/validar": validar_view(page),
        "/cadastro": cadastro_view(page),
    }

    def route_change(event: ft.RouteChangeEvent):
        route = event.route  # Pegamos a string da rota corretamente
        if route.startswith("/ingresso/"):
            codigo_ingresso = route.split("/")[-1]  # Pega o código do ingresso da URL
            ingresso_data = {"codigo_ingresso": codigo_ingresso}  # Aqui você pode preencher com mais dados se necessário
            page.views.clear()
            page.views.append(ingresso_view(page, ingresso_data))  # Passa os dados do ingresso para a view
            page.update()
        elif route in views:
            page.views.clear()
            page.views.append(views[route])
            page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)
