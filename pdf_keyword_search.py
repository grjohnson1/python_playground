import os
import csv
import logging
import pdfplumber
from rapidfuzz import fuzz

# Suppress pdfminer log messages
logging.getLogger("pdfminer").setLevel(logging.ERROR)

# Folder containing PDFs
folder_path = "resumes"
# Output CSV file
output_csv = "results_by_file.csv"

def search_keywords_in_pdf(pdf_path, keywords, threshold=85):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text += text + " "
        full_text_lower = full_text.lower()
        matched_keywords = []
        for keyword in keywords:
            score = fuzz.partial_ratio(keyword.lower(), full_text_lower)
            if score >= threshold:
                matched_keywords.append(keyword)
        return matched_keywords
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

    results = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            full_path = os.path.join(folder_path, filename)
            matched = search_keywords_in_pdf(full_path, keywords)
            if matched:
                print(f"{filename}: Matched -> {', '.join(matched)}")
            else:
                print(f"{filename}: No keywords matched.")
            results.append({
                "File Name": filename,
                "Matched Keywords": ", ".join(matched) if matched else "None"
            })

    # Write results to CSV
    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["File Name", "Matched Keywords"])
        writer.writeheader()
        writer.writerows(results)

    print(f"\n✅ Results saved to {output_csv}")

if __name__ == "__main__":
    main()
