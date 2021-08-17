import fitz

pdf_file = fitz.open('lyrics.pdf')

for pageNumbers, page in enumerate(pdf_file.pages(), start=1):
    text = page.getText()
    print(text)

for i in range(len(pdf_file)):
    for img in pdf_file.getPageImageList(i):
        xref = img[0]
        pix = fitz.Pixmap(pdf_file, xref)

        if pix.n < 5:
            pix = fitz.Pixmap(fitz.csRGB, pix)
        pix.writePNG("p%s-%s.png" % (i, xref))