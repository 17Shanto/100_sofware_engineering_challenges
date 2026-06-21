import fitz

def convert_pdf_to_text()->str:
    resume_path = "Alve Ibrahim_CV - Alvee Ibrahim.pdf"
    doc = fitz.open(resume_path)
    extracted_text = ""
    for page in doc:
        extracted_text += str(page.get_text())
    doc.close()
    return extracted_text

import fitz

def save_to_output_txt():
    resume_path = "Alve Ibrahim_CV - Alvee Ibrahim.pdf"
    output_path = "output.txt"
    
    # Extract text from the PDF
    doc = fitz.open(resume_path)
    extracted_text = ""
    for page in doc:
        extracted_text += str(page.get_text())
    doc.close()
    
    # Save the extracted text to a text file
    with open(output_path, "w", encoding="utf-8") as text_file:
        text_file.write(extracted_text)

