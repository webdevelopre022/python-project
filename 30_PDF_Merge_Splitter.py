import PyPDF2

def split_pdf(file_path, output_folder):
    with open(file_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for i in range(len(reader.pages)):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[i])
            output_filename = f"{output_folder}/page_{i+1}.pdf"
            with open(output_filename, 'wb') as output_pdf:
                writer.write(output_pdf)
            print(f"Saved: {output_filename}")

# Example usage
split_pdf('merged_output.pdf', 'split_pages')
