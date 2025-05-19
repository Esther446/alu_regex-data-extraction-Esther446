import re
import sys

def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return re.findall(pattern, text)

def extract_urls(text):
    pattern = r'https?://[^\s"]+|www\.[^\s"]+'
    return re.findall(pattern, text)

def extract_phones(text):
    pattern = r'(\+?\d{1,3}[\s.-]?)?(\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}'
    return re.findall(pattern, text)

def extract_credit_cards(text):
    pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'
    return re.findall(pattern, text)

def extract_times(text):
    pattern = r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?: ?[APap][Mm])?\b'
    return re.findall(pattern, text)

def extract_html_tags(text):
    pattern = r'<\s*([a-zA-Z][a-zA-Z0-9]*)\b[^>]*>'
    return re.findall(pattern, text)

def extract_hashtags(text):
    pattern = r'#\w+'
    return re.findall(pattern, text)

def extract_currency(text):
    pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(pattern, text)

def format_output(title, results):
    output = f"{title} ({len(results)} found):\n" + "-"*40 + "\n"
    for item in results:
        clean_item = item if isinstance(item, str) else ''.join(item)
        output += f"  • {clean_item.strip()}\n"
    return output + "\n"

def extract_all(text):
    results = ""
    results += format_output("EMAIL matches", extract_emails(text))
    results += format_output("URL matches", extract_urls(text))
    results += format_output("PHONE NUMBER matches", extract_phones(text))
    results += format_output("CREDIT CARD matches", extract_credit_cards(text))
    results += format_output("CURRENCY matches", extract_currency(text))
    results += format_output("TIME matches", extract_times(text))
    results += format_output("HTML TAG matches", extract_html_tags(text))
    results += format_output("HASHTAG matches", extract_hashtags(text))
    return results

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 regex_data_extractor.py <yourfile.txt>")
        return

    filepath = sys.argv[1]

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()

        print("\n=== EXTRACTION RESULTS ===\n")
        output = extract_all(text)
        print(output)

        # Save to file
        with open("extraction_results.txt", "w", encoding='utf-8') as f:
            f.write(output)
            print("✅ Results saved to 'extraction_results.txt'.")

    except FileNotFoundError:
        print(f"❌ File '{filepath}' not found.")
    except Exception as e:
        print(f"⚠️ Error reading file: {e}")

if __name__ == "__main__":
    main()

