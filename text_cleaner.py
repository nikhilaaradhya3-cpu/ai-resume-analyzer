import re

def clean_resume_text(text):
    """
    Cleans and normalizes extracted resume text.
    Converts to lowercase, removes special characters, but retains 
    important technical symbols (like C++, C#, .NET).
    """
    if not text:
        return ""

    # Convert text to lowercase for uniform comparison
    text = text.lower()

    # Remove URLs and email addresses to avoid matching irrelevant data
    text = re.sub(r'http\S+|www\S+|[\w\.-]+@[\w\.-]+', ' ', text)

    # Remove unnecessary symbols but keep alphanumeric, spaces, and specific symbols (+, #, .) 
    # This ensures "c++", "c#", and ".net" are retained perfectly
    text = re.sub(r'[^a-z0-9\s+#.]', ' ', text)

    # Remove repeated spaces and newlines
    text = re.sub(r'\s+', ' ', text).strip()

    return text