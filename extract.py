from PyPDF2 import PdfFileReader
from pathlib import Path

# Create pdf file reader object
pdf = PdfFileReader(
    "Lemony Snicket - The Bad Beginning (A Series of Unfortunate Events, Book 1) (1999).pdf")

# grab the page(s)
number_page = 9
page_1_object = pdf.getPage(number_page)


# extract text
page_1_text = page_1_object.extractText()
print(page_1_text)


with Path(f"paragraph-page-{number_page}.txt").open(mode='w') as output_file:
    text = pdf.getPage(number_page).extractText()
    output_file.write(text)
