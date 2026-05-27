import os

from agent.pdf_generator import generate_medical_report_pdf


def save_report_as_pdf(report_text: str) -> str:

    reports_folder = "agent/reports"

    os.makedirs(reports_folder, exist_ok=True)

    pdf_path = os.path.join(
        reports_folder,
        "medical_report.pdf"
    )

    generate_medical_report_pdf(
        report_text,
        output_path=pdf_path
    )

    return f"""
✅ PDF report generated successfully.

📁 Saved Location:
{pdf_path}
"""