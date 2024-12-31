import random
from fpdf import FPDF

def generate_multiplication_pdf(base_number, filename="multiplication_practice.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=36)
    
    pdf.cell(200, 10, txt="Multiplication Practice!", ln=True, align='C')
    pdf.ln(10)
    
    questions_per_column = 10
    column_width = 95
    
    pdf.set_font("Arial", size=24)
    
    for i in range(questions_per_column):
        multiplier1 = random.randint(0, 12)
        multiplier2 = random.randint(0, 12)
        question1 = f"{base_number} x {multiplier1} = "
        question2 = f"{base_number} x {multiplier2} = "
        
        pdf.cell(column_width, 10, txt=question1, ln=0)
        pdf.cell(column_width, 10, txt=question2, ln=1)
        pdf.ln(10)  # Add double line spacing
    
    pdf.output(filename)
    print(f"PDF generated: {filename}")

if __name__ == "__main__":
    base_number = int(input("Enter the base number for multiplication practice: "))
    generate_multiplication_pdf(base_number)