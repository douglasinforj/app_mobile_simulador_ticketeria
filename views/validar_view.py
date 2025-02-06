import flet as ft
from components.navbar import navbar
from services.api_service import validar_ingresso
import qrcode  # Para escanear QR Code

def validar_view(page):
    # Campo de entrada para código de ingresso
    codigo_input = ft.TextField(label="Código do Ingresso", autofocus=True)
    
    # Função que vai chamar a API para validar o ingresso
    def handle_validar(e):
        codigo = codigo_input.value.strip()
        if codigo:
            response = validar_ingresso(codigo)
            
            if response["status"]:
                # Se o ingresso for válido, exibe a caixa de diálogo com o nome e CPF do cliente
                dialog = ft.AlertDialog(
                    title="Validação do Ingresso",
                    content=ft.Column([
                        ft.Text(f"Ingresso válido!"),
                        ft.Text(f"Nome: {response['mensagem'].split(' - ')[0].split(': ')[1]}"),
                        ft.Text(f"CPF: {response['mensagem'].split(' - ')[1]}"),
                    ]),
                    actions=[
                        ft.TextButton("Fechar", on_click=lambda e: dialog.close())
                    ]
                )
                page.add(dialog)
                dialog.open = True
            else:
                # Exibe uma caixa de diálogo para ingressos inválidos
                dialog = ft.AlertDialog(
                    title="Validação do Ingresso",
                    content=ft.Text(response["mensagem"]),
                    actions=[
                        ft.TextButton("Fechar", on_click=lambda e: dialog.close())
                    ]
                )
                page.add(dialog)
                dialog.open = True

            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, insira um código de ingresso válido!", color="red"))
            page.snack_bar.open = True
            page.update()

    # Função para escanear o QR Code e extrair o código do ingresso
    def handle_scan_qr(e):
        # Aqui você deve implementar a leitura do QR Code, com alguma biblioteca de escaneamento
        # Como exemplo: `qrcode.read(qr_img_path)`
        codigo_lido = "Código extraído do QR Code"  # Aqui você deve obter o código real a partir da câmera ou imagem
        response = validar_ingresso(codigo_lido)
        
        if response["status"]:
            dialog = ft.AlertDialog(
                title="Validação do Ingresso",
                content=ft.Column([
                    ft.Text(f"Ingresso válido!"),
                    ft.Text(f"Nome: {response['mensagem'].split(' - ')[0].split(': ')[1]}"),
                    ft.Text(f"CPF: {response['mensagem'].split(' - ')[1]}"),
                ]),
                actions=[
                    ft.TextButton("Fechar", on_click=lambda e: dialog.close())
                ]
            )
            page.add(dialog)
            dialog.open = True
        else:
            dialog = ft.AlertDialog(
                title="Validação do Ingresso",
                content=ft.Text(response["mensagem"]),
                actions=[
                    ft.TextButton("Fechar", on_click=lambda e: dialog.close())
                ]
            )
            page.add(dialog)
            dialog.open = True

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
