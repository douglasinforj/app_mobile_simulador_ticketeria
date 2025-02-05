# mensagens de feedback

import flet as ft 

def show_snack_bar(page, message, success=True):
    page.snack_bar = ft.SnackBar(ft.Text(message, color="green" if success else "red"))
    page.snack_bar.open = True
    page.update()