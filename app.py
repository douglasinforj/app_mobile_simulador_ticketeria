import flet as ft 

from views.home_view import home_view
from views.comprar_view import comprar_view
from views.validar_view import validar_view

def main(page: ft.Page):
    page.title = "Ticket APP"
    page.theme_mode = ft.ThemeMode.LIGHT

    def route_change(route):
        page.views.clear()
        if route == "/":
            page.views.append(home_view(page))
        elif route  == "/comprar":
            page.views.append(comprar_view(page))
        elif route == "/validar":
            page.views.append(validar_view(page))
        page.update()
    
    page.on_route_change = route_change
    page.go("/")



ft.app(target=main)