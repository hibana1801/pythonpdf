import PyPDF2
import tkinter as tkr
from tkinter import *
from tkinter import filedialog

"""Window"""
pdfread = Tk()
pdfread.title("PDF Read")
pdfread.geometry("800x500")

"""Text box"""
my_file = Text(pdfread, height=30, width=80)
my_file.pack(padx=10)

"""Open PDF button"""


def open_btn():
    open_pdf = filedialog.askopenfilename(
        initialdir="Desktop",
        title="Open PDF",
        filetypes=(
            ("PDF File", "*.pdf"),
            ("All files", "*.all")))

    pdf_file = PyPDF2.PdfFileReader(open_pdf)
    for i in range(pdf_file.getNumPages() - 1):
        page = pdf_file.getPage(i)
        page_content = page.extractText()
        my_file.insert(1.0, page_content)


Open = tkr.Button(pdfread, width=5, height=3, text="Open", command=open_btn)
Open.place(x=20, y=20)

pdfread.mainloop()
