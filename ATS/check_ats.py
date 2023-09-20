import PyPDF2
import re

def is_ats_friendly(pdf_path):
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            
            # Check if the PDF has selectable text
            if pdf_reader.isEncrypted:
                return False, "PDF is encrypted"
            
            text = ""
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                text += page.extractText()
            
            # Check for basic formatting guidelines (you can customize this)
            if len(text) < 100:  # Check if the document has sufficient content
                return False, "PDF has insufficient content"
            
            if not any(c.isalnum() for c in text):  # Check for alphanumeric characters
                return False, "PDF does not contain alphanumeric characters"
            
            # Check for common ATS-unfriendly elements
            # if re.search(r'[^ -~\n\r]+', text):  # Check for non-ASCII characters
            #     return False, "PDF contains non-ASCII characters"

            if re.search(r'(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})', text):  # Check for dates in non-standard formats
                return False, "PDF contains non-standard date formats"
            
            return True, "PDF is ATS-friendly"
    except Exception as e:
        return False, str(e)

def main(pdf_path):
    is_friendly, message = is_ats_friendly(pdf_path)

    if is_friendly:
        print("The PDF is ATS-friendly.")
    else:
        print(f"The PDF is not ATS-friendly: {message}")

if __name__ == "__main__":
    pdf_path = "resume.pdf"  # Replace with the path to your PDF resume
    main(pdf_path)
