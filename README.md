Regex Data Extraction is a simple and effective Python script designed to extract common types of data from large amounts of text using regular expressions. This tool can help you find and validate useful information like email addresses, URLs, phone numbers, credit card numbers, time formats, HTML tags, hashtags, and currency amounts quickly and accurately.

What this script does is scan through any given text and extracts the following data types using regex patterns:

Email addresses (e.g., user@example.com, firstname.lastname@company.co.uk)

URLs (e.g., https://www.example.com, https://subdomain.example.org/page)

Phone numbers in various common formats (e.g., (123) 456-7890, 123-456-7890, 123.456.7890)

Credit card numbers formatted with spaces or dashes (e.g., 1234 5678 9012 3456, 1234-5678-9012-3456)

Time in 24-hour or 12-hour formats (e.g., 14:30, 2:30 PM)

HTML tags (e.g., <p>, <div class="example">)

Hashtags (e.g., #example, #ThisIsAHashtag)

Currency amounts formatted in US style (e.g., $19.99, $1,234.56)

Clone the repository to your local machine;

git clone https://github.com/Esther446/alu_regex-data-extraction-Esther446.git

Navigate to the project folder;

cd alu_regex-data-extraction-Esther446

Run the script on a sample text file or your own file;

python3 regex_extractor.py

To extract data from a specific file, provide the filename as an argument;
python3 regex_extractor.py output.txt

When you run the script, it will display the data it found in a clear, organized manner:

 EXTRACTION RESULTS

EMAIL matches (2 found):
----------------------------------------
  • user@example.com
  • firstname.lastname@company.co.uk

URL matches (2 found):
----------------------------------------
  • https://www.example.com
  • https://subdomain.example.org/page
...

