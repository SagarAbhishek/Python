import PyPDF2
from PyPDF2 import PdfFileMerger

#Create an instance of PdfFileMerger() class
merger =PyPDF2.PdfMerger()

pdf_files = ['Project Of Python\PDF merger\sample_page1.pdf', 'Project Of Python\PDF merger\sample_page2.pdf','Project Of Python\PDF merger\sample_page3.pdf']
destinationPath="Project Of Python\PDF merger\merged_2_pages.pdf"
#Iterate over the list of the file paths
for pdf_file in pdf_files:
    #Append PDF files
    pdfFile=open(pdf_file,'rb')
    pdfReader=PyPDF2.PdfReader(pdfFile)
    merger.append(pdf_file)

merger.write(destinationPath)
merger.close()