import pdfplumber


with pdfplumber.open("./data/US-Constitution.pdf") as pdf, open("./output/US-Constitution.txt", "w", encoding='utf-8') as file: 

    for page in pdf.pages:
        t = page.extract_text()
        if t:
            file.write(t + '\n')
