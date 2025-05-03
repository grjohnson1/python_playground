import os
import pdfplumber

# Folder containing PDFs
folder_path = "resumes"

def search_keywords_in_pdf(pdf_path, keywords):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            for page in pdf.pages:
                full_text += page.extract_text() or ""
        # Search for keywords (case-insensitive)
        found = [word for word in keywords if word.lower() in full_text.lower()]
        return found
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return []

def main():
    # Get user input for keywords
    user_input = input("Enter keywords to search for (comma-separated): ")
    keywords = [k.strip() for k in user_input.split(",") if k.strip()]
    
    if not keywords:
        print("No keywords entered. Exiting.")
        return

    print(f"\nSearching for: {', '.join(keywords)}\n")
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            full_path = os.path.join(folder_path, filename)
            found_words = search_keywords_in_pdf(full_path, keywords)
            if found_words:
                print(f"{filename}: Found -> {', '.join(found_words)}")
            else:
                print(f"{filename}: No keywords found.")

if __name__ == "__main__":
    main()