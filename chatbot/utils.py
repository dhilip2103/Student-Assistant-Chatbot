import os
import pdfplumber
import docx2txt

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for p in pdf.pages:
                page_text = p.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    elif ext in [".docx", ".doc"]:
        return docx2txt.process(file_path)
    else:
        # fallback try PyPDF2 if pdfplumber fails, but return empty if none
        return ""
