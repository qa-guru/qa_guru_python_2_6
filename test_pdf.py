import os.path

from PyPDF2 import PdfReader
# docs_pdf_path = os.path.abspath(__file__) + 'resources' + 'docs-pytest-org-en-latest.pdf'
pdf_reader = PdfReader('./resources/docs-pytest-org-en-latest.pdf')
number_of_pages = len(pdf_reader.pages)

assert number_of_pages == 412
page = pdf_reader.pages[0]
text = page.extract_text()
print(text)
assert 'Jul 11, 2022' in text