from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Create PDF
pdf = SimpleDocTemplate("invoice.pdf", pagesize=letter)

styles = getSampleStyleSheet()
elements = []

title = Paragraph("Invoice Report", styles['Title'])
elements.append(title)

elements.append(Spacer(1, 20))

content = Paragraph(
    "Hello Abdul, this PDF was generated using Python ReportLab.",
    styles['BodyText']
)

elements.append(content)

# Build PDF
pdf.build(elements)

print("PDF generated successfully!")