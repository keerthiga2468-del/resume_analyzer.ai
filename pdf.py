from pypdf import PdfReader

def extract_text(pdf_doc):  # to extract the raw text from the input pdf
    try:
        pdf = PdfReader(pdf_doc)
        
        raw_text = ""
        for index,page in enumerate(pdf.pages): 
            # get by index and respective text of the pages in pdf
            text = page.extract_text() # to get only text from the pages
            if text: # if pages contains text it will get added to raw text
                raw_text += text
        return raw_text

    except Exception as e: # error for unprocessed file
        return f"Error in extracting text"
    