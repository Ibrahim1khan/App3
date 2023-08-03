from fpdf import FPDF
import pandas as pd #it is a data analysis library
from random import randint

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)


df = pd.read_csv("topics.csv")
print(df.keys())

for index, row in df.iterrows():
    
    for i in range(row["Pages"]):
        pdf.add_page()
        pdf.set_text_color(randint(0,255), randint(0,255), randint(0,255)) #adding color the text
        pdf.set_font(family="Times", style="B", size=12)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0) #adding lines of text
        pdf.cell(w=0, h=12, txt=str(row["Order"]), align="L", ln=1, border=0)
        
        pdf.line(10 ,20, 200, 21)

        pdf.ln(240)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(randint(0,255), randint(0,255), randint(0,255)) #adding color the text
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


pdf.output("output.pdf")