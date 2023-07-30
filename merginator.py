import PyPDF2

def merge_pdfs(pdf_list, output_filename):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf_file in pdf_list:
        with open(pdf_file, 'rb') as file:
            pdf_merger.append(file)

    with open(output_filename, 'wb') as output_file:
        pdf_merger.write(output_file)

if __name__ == '__main__':
    print(r'''
   _____          __  __ _
  / ____|   /\   |  \/  (_)
 | |  __   /  \  | \  / |_ _ __
 | | |_ | / /\ \ | |\/| | | '_ \
 | |__| |/ ____ \| |  | | | | | |
  \_____/_/    \_\_|  |_|_|_| |_| big companies that monopolize and charge too much for simple shit liek this v1.0

''')
    print("Welcome to the PDF Merger!")
    print("Please follow the instructions below to merge your PDF files.")
    print("--------------------------------------------------------------")

    num_pdfs = int(input("Enter the total number of PDF files you want to merge: "))
    pdf_files = []

    for i in range(1, num_pdfs + 1):
        pdf_file = input(f"Enter the path of PDF file {i}: ")
        pdf_files.append(pdf_file)

    output_filename = input("Enter the output filename for the combined PDF: ")

    merge_pdfs(pdf_files, output_filename)

    print("--------------------------------------------------------------")
    print("PDF files successfully merged into:", output_filename)
    print("Thank you for using the PDF Merger!")

     
