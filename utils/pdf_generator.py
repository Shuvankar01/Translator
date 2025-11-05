from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

def generate_pdf(name, content):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    p.setFont("Helvetica-Bold", 18)
    p.drawString(50, height - 80, name)
    p.setFont("Helvetica", 11)
    text = p.beginText(50, height - 120)
    for line in content.split("\n"):
        text.textLine(line.strip())
    p.drawText(text)
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    return pdf
