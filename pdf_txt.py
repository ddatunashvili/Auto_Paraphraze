# convert pdf to text



# with open(r'book.pdf', 'r') as f:
#     print(f.read())

from PyPDF2 import PdfReader

def pdf_txt():
    reader = PdfReader(r"book.pdf")
    number_of_pages = len(reader.pages)

    pages = []
    # all_text = ""
    for page in  reader.pages:
        pages.append(page.extract_text())
        # all_text += page.extract_text()



    with open(r'pages.txt', 'w', encoding="utf-8") as f:
        f.writelines(pages)

    # with open(r'all_text.txt', 'w', encoding="utf-8") as f:
        # f.write(all_text)
        
    