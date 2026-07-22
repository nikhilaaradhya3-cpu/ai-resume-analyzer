import pypdf
import docx

def extract_text_from_pdf(file):
    """
    Extracts text from every page of a PDF file.
    """
    text = ""
    try:
        reader = pypdf.PdfReader(file)
        for page in reader.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + "\n"
    except Exception as e:
        return f"Error reading PDF: {e}"
    
    return text

def extract_text_from_docx(file):
    """
    Extracts text from every paragraph of a DOCX file.
    """
    text = ""
    try:
        doc = docx.Document(file)
        for para in doc.paragraphs:
            if para.text:
                text += para.text + "\n"
    except Exception as e:
        return f"Error reading DOCX: {e}"
    
    return text

def extract_resume_text(file, file_name):
    """
    Routes the uploaded file to the correct extraction function based on its extension.
    """
    # Ensure the file pointer is at the beginning before reading
    file.seek(0) 
    
    file_extension = file_name.lower()
    
    if file_extension.endswith('.pdf'):
        return extract_text_from_pdf(file)
    elif file_extension.endswith('.docx'):
        return extract_text_from_docx(file)
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or DOCX file.")