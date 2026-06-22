from src.cv.cv_chain import gist_chain
from src.pdf_to_text.pdf_to_txt import save_to_output_txt, convert_pdf_to_text


cv_text = convert_pdf_to_text()
response = gist_chain.invoke({"cv_text": cv_text})
print(response)