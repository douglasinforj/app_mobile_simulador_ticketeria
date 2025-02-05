import flet as ft
from components.navbar import navbar
from services.api_service import validar_ingresso
import qrcode  # Adicionar qrcode para gerar QR

def validar_view(page):
    # Campo de entrada para código de ingresso
    codigo_input = ft.TextField(label="Código do Ingresso", autofocus=True)
    
    # Função que vai chamar a API para validar o ingresso
    def handle_validar(e):
        codigo = codigo_input.value.strip()
        if codigo:
            response = validar_ingresso(codigo)
            page.snack_bar = ft.SnackBar(ft.Text(response["mensagem"], color="green" if response["status"] else "red"))
            page.snack_bar.open = True
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, insira um código de ingresso válido!", color="red"))
            page.snack_bar.open = True
            page.update()

    # Função para escanear o QR Code e extrair o código do ingresso
    def handle_scan_qr(e):
        #TODO: Verifica
        # Aqui você deve implementar a leitura do QR Code, que você pode fazer com alguma biblioteca de escaneamento
        # Como exemplo: `qrcode.read(qr_img_path)`
        codigo_lido = "Código extraído do QR Code"  # Aqui você deveria obter o código real a partir da câmera ou da imagem
        response = validar_ingresso(codigo_lido)
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
            ft.ElevatedButton("Escanear QR Code", on_click=handle_scan_qr),  # Adicionando o botão de escanear
            ft.ElevatedButton("Voltar", on_click=lambda _: page.go("/")),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )
