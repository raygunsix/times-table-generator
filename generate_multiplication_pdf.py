import random
from fpdf import FPDF

def generate_multiplication_pdf(base_number, filename="multiplication_practice.pdf"):
    pdf = FPDF()
    pdf.add_page()
    
    # Add image and title in separate columns
    pdf.set_font("Arial", size=32)
    pdf.cell(10, 20, txt="", border=0)  # Empty cell for spacing
    pdf.multi_cell(100, 20, txt="Multiplication Practice!", align='L', border=0)
    pdf.image("images/math-mental-abuse.jpg", x=120, y=10, w=70)
    pdf.ln(20)
    
    questions_per_column = 10
    column_width = 95
    
    pdf.set_font("Arial", size=24)
    
    for i in range(questions_per_column):
        multiplier1 = random.randint(0, 12)
        multiplier2 = random.randint(0, 12)
        question1 = f"{base_number} x {multiplier1} = "
        question2 = f"{base_number} x {multiplier2} = "

        pdf.ln(10) # Add line spacing      
        pdf.cell(10, 10, txt="", border=0)  # Empty cell for spacing
        pdf.cell(column_width, 10, txt=question1, ln=0)
        pdf.cell(column_width, 10, txt=question2, ln=1)
    
    pdf.output(filename)
    print(f"PDF generated: {filename}")

if __name__ == "__main__":
    base_number = int(input("Enter the base number for multiplication practice: "))
    generate_multiplication_pdf(base_number)