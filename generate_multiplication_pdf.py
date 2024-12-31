import random
from fpdf import FPDF

def generate_multiplication_pdf(base_number, filename="multiplication_practice.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Multiplication Practice", ln=True, align='C')
    pdf.ln(10)
    
    for i in range(1, 21):  # Generate 20 questions
        multiplier = random.randint(0, 12)
        question = f"{base_number} x {multiplier} = "
        pdf.cell(200, 10, txt=question, ln=True)
    
    pdf.output(filename)
    print(f"PDF generated: {filename}")

if __name__ == "__main__":
    base_number = int(input("Enter the base number for multiplication practice: "))
    generate_multiplication_pdf(base_number)