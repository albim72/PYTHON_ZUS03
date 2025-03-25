from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def generate_pdf(filename):

    #rejestracja czcionki
    pdfmetrics.registerFont(TTFont('DejaVu','DejaVuSans.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVuB','DejaVuSansMono-Bold.ttf'))
    c = canvas.Canvas(filename,pagesize=A4)
    width,height = A4

    #dodanie tytułu
    c.setFont("DejaVuB",20)
    c.drawCentredString(width/2,height-100,"Raport - Python!")

    #dodanie zwykłego tekstu
    c.setFont("DejaVu",12)
    c.drawString(100,height-150,"To jest przykładowy PDF w Pythonie.")
    c.drawString(100,height-170,"Możesz dodac teskt, obrazy i więcej...")

    #dodanie obrazu
    c.drawImage("pngtree.png",100,height-800)
    #dodanie prostokąta
    c.showPage()
    c.save()

    print(f"PDF {filename} został wygenerowany")

generate_pdf("raport_z_obrazem.pdf")
