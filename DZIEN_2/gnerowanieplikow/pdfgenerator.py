from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

class PdfGenerator:
    def generate(self,data,filename):
        c = canvas.Canvas(filename,pagesize=A4)
        width,height = A4
        
        c.setFont("Helvetica",12)
        c.drawString(50,height-50,"Raport specjalny!")
        y = height -80
        for record in data:
            c.drawString(50,y,str(record))
            y -= 20
        c.save()
        print(f"PDF zapisany do {filename}")
