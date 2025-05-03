import os
import pdfplumber
from rapidfuzz import fuzz

# Folder containing PDFs
folder_path = "resumes"

def search_keywords_in_pdf(pdf_path, keywords, threshold=85):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            for page in pdf.pages:
                full_text += page.extract_text() or ""
        full_text_lower = full_text.lower()
        found = []
        for word in keywords:
            for chunk in full_text_lower.split():
                score = fuzz.partial_ratio(word.lower(), chunk)
                if score >= threshold:
                    found.append(word)
                    break
        return found
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return []

def main():
    user_input = input("Enter keywords to search for (comma-separated): ")
    keywords = [k.strip() for k in user_input.split(",") if k.strip()]
    
    if not keywords:
        print("No keywords entered. Exiting.")
        return

    print(f"\nFuzzy searching for: {', '.join(keywords)}\n")
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            full_path = os.path.join(folder_path, filename)
            found_words = search_keywords_in_pdf(full_path, keywords)
            if found_words:
                print(f"{filename}: Approx match found for -> {', '.join(found_words)}")
            else:
                print(f"{filename}: No matching keywords found.")

if __name__ == "__main__":
    main()
