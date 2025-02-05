import flet as ft
from views.home_view import home_view
from views.comprar_view import comprar_view
from views.validar_view import validar_view

def main(page: ft.Page):
    page.title = "Ticket App 🎟️"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Criar as views uma única vez
    views = {
        "/": home_view(page),
        "/comprar": comprar_view(page),
        "/validar": validar_view(page),
    }

    def route_change(event: ft.RouteChangeEvent):
        route = event.route  # Pegamos a string da rota corretamente
        if route in views:
            page.views.clear()
            page.views.append(views[route])
            page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)
