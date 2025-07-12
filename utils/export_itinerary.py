from fpdf import FPDF
import streamlit as st

def export_pdf(text, state):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Incredible India Trip to {state}\n\n{text}")
    path = f"{state}_itinerary.pdf"
    pdf.output(path)
    with open(path, "rb") as f:
        st.download_button("Download PDF", f, file_name=path)
