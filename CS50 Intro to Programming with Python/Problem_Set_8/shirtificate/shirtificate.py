from fpdf import FPDF

class PDF():
    def __init__(self, name):
        #creates PDF
        self._pdf = FPDF()
        #creates blank page
        self._pdf.add_page()
        #sets a font for the text
        self._pdf.set_font("helvetica", "B", 50)
        #is the text that is at the top of the page
        self._pdf.cell(0, 50, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align="C")
        #adds the image which is centered horizontally
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        #sets the font size to another size
        self._pdf.set_font_size(25)
        #Ensures the text is white text
        self._pdf.set_text_color(255, 255, 255)
        #The text which is on the shirt
        self._pdf.text(x=50, y=120, txt=f"{name} took CS50")

    #Responsible for the output file
    def save(self, name):
        self._pdf.output(name)

#Input of a name which is then put on a shirt in an image
name = input("Name: ")
pdf=PDF(name)
pdf.save("shirtificate.pdf")