from fpdf import FPDF

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

pdf.set_font("Helvetica", "B", 16)
pdf.cell(0, 10, "Acme Cloud India - Employee Handbook", ln=True)
pdf.ln(4)

pdf.set_font("Helvetica", "", 12)
handbook_text = (
    "1. Work Mode & Core Hours:\n"
    "Acme Cloud India operates on a hybrid schedule with 3 office days per week "
    "(Tuesday, Wednesday, and Thursday) from Bengaluru or Gurugram hubs. "
    "Core collaboration hours are 10:30 AM to 4:30 PM IST.\n\n"
    "2. Leave & Holiday Policy:\n"
    "Full-time employees receive 24 earned leaves per calendar year plus national "
    "and regional public holidays. Unused earned leave up to 10 days can carry "
    "forward into the next year.\n\n"
    "3. Learning & Certification Allowance:\n"
    "Each engineer gets an annual learning stipend of INR 35,000 for cloud, "
    "AI/ML, or data engineering courses and certifications upon manager approval."
)
pdf.multi_cell(0, 7, handbook_text)
pdf.output("data/company_handbook.pdf")
print("Generated data/company_handbook.pdf successfully.")