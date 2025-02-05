import flet as ft
import qrcode  # Para gerar o QR Code
from components.navbar import navbar
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# Função para gerar o QR Code com base no código do ingresso e salvar na pasta assets/qrcode
def gerar_qrcode(codigo_ingresso):
    # Definindo o caminho para salvar na pasta 'assets/qrcode'
    qr_dir = "assets/qrcode"
    if not os.path.exists(qr_dir):
        os.makedirs(qr_dir)

    qr_path = os.path.join(qr_dir, f"qr_code_{codigo_ingresso}.png")  # Caminho completo para o QR Code
    qr_img = qrcode.make(codigo_ingresso)  # Gera o QR Code com base no código
    qr_img.save(qr_path)  # Salva o QR Code como imagem
    return qr_path

# Função para gerar o PDF com o QR Code e os dados do ingresso
def gerar_pdf(codigo_ingresso, nome_comprador, cpf_comprador, qr_path):
    pdf_path = f"assets/{codigo_ingresso}_ingresso.pdf"  # Caminho para salvar o PDF
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Adicionando texto no PDF
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, f"Ingresso Confirmado!")
    c.drawString(100, 730, f"Código do ingresso: {codigo_ingresso}")
    c.drawString(100, 710, f"Nome do Comprador: {nome_comprador}")
    c.drawString(100, 690, f"CPF do Comprador: {cpf_comprador}")
    
    # Adicionando o QR Code no PDF
    c.drawImage(qr_path, 100, 600, width=150, height=150)

    # Salvando o PDF
    c.save()
    return pdf_path

# Função para exibir o ingresso com QR Code e dados do comprador
def ingresso_view(page, ingresso_data):
    codigo_ingresso = ingresso_data.get("codigo_ingresso", "Código não encontrado")
    nome_comprador = ingresso_data.get("nome", "Nome não encontrado")
    cpf_comprador = ingresso_data.get("cpf", "CPF não encontrado")

    # Gerar o QR Code
    qr_path = gerar_qrcode(codigo_ingresso)

    # Gerar o PDF
    pdf_path = gerar_pdf(codigo_ingresso, nome_comprador, cpf_comprador, qr_path)

    return ft.View(
        "/ingresso",
        controls=[
            navbar(page),
            ft.Text(f"Ingresso Confirmado!", size=24, weight=ft.FontWeight.BOLD),
            ft.Text(f"Código do ingresso: {codigo_ingresso}", size=10, color="blue"),
            ft.Text(f"Nome do Comprador: {nome_comprador}", size=14),
            ft.Text(f"CPF do Comprador: {cpf_comprador}", size=14),
            ft.Image(src=qr_path),  # Exibe o QR Code gerado
            ft.ElevatedButton("Voltar", on_click=lambda _: page.go("/")),
            ft.ElevatedButton("Baixar PDF", on_click=lambda _: page.download(pdf_path))  # Correção aqui
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )
