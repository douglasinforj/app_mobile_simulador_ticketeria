import flet as ft
import qrcode  # Para gerar o QR Code
from components.navbar import navbar

# Função para gerar o QR Code com base no código do ingresso
def gerar_qrcode(codigo_ingresso):
    qr_img = qrcode.make(codigo_ingresso)  # Gera o QR Code com base no código
    qr_path = f"qr_code_{codigo_ingresso}.png"  # Nome do arquivo com base no código do ingresso
    qr_img.save(qr_path)  # Salva o QR Code como imagem
    return qr_path

# Função para exibir o ingresso com QR Code e dados do comprador
def ingresso_view(page, ingresso_data):
    codigo_ingresso = ingresso_data.get("codigo_ingresso", "Código não encontrado")
    nome_comprador = ingresso_data.get("nome", "Nome não encontrado")
    cpf_comprador = ingresso_data.get("cpf", "CPF não encontrado")

    # Gerar o QR Code
    qr_path = gerar_qrcode(codigo_ingresso)

    return ft.View(
        "/ingresso",
        controls=[
            navbar(page),
            ft.Text(f"Ingresso Confirmado!", size=24, weight=ft.FontWeight.BOLD),
            ft.Text(f"Código do ingresso: {codigo_ingresso}", size=10, color="blue"),
            ft.Text(f"Nome do Comprador: {nome_comprador}", size=14),
            ft.Text(f"CPF do Comprador: {cpf_comprador}", size=14),
            ft.Image(src=qr_path),  # Exibe o QR Code gerado
            ft.ElevatedButton("Voltar", on_click=lambda _: page.go("/"))
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )
