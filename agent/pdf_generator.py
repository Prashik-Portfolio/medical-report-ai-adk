from fpdf import FPDF
from datetime import datetime


def generate_medical_report_pdf(report_text, output_path="medical_report.pdf"):
    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "AI Preliminary Radiology Report", ln=True, align="C")

    pdf.ln(10)

    pdf.set_font("Arial", "", 12)

    current_date = datetime.now().strftime("%Y-%m-%d %H:%M")

    pdf.cell(200, 10, f"Generated On: {current_date}", ln=True)

    pdf.ln(5)

    # Multi-line report content
    pdf.multi_cell(0, 8, report_text)

    pdf.ln(10)

    pdf.set_font("Arial", "I", 10)

    disclaimer = (
        "Disclaimer: This report is AI-generated and intended "
        "for preliminary assistance only. It is not a certified "
        "medical diagnosis."
    )

    pdf.multi_cell(0, 6, disclaimer)

    pdf.output(output_path)

    return output_path