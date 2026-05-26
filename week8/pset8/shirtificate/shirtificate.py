from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="P", format="A4")
pdf.add_page()
pdf.set_font("Helvetica", "B", 32)
pdf.cell(0, 40, "CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", x=30, y=70, w=150)
pdf.set_font("Helvetica", "B", 24)
pdf.set_text_color(255, 255, 255)
pdf.cell(-190, 210, name, align="C")
pdf.output("shirtificate.pdf")
