from reportlab.pdfgen import canvas

pdf = canvas.Canvas("sample.pdf")

pdf.drawString(
    100,
    750,
    "Hello Abdul"
)

pdf.save()

print("PDF Created")