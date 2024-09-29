
"""
 You have a text document that contains dates in various formats such as 12/09/2023, 2023-09-12, and Sep 12,  2023. Write a Python script that uses regular expressions to extract all dates in these formats from the text.
"""

import re

# Sample text containing various date formats
text = """
Today is 12/09/2023. The event was scheduled for 2023-09-12.
There is another meeting on Sep 12, 2023 and an earlier one on 09/11/2022.
Don't forget about the task due on October 1, 2023.
"""

# Regular expressions for different date formats
regex_patterns = [
    r'\b\d{2}/\d{2}/\d{4}\b',         # Matches dates in MM/DD/YYYY or DD/MM/YYYY format
    r'\b\d{4}-\d{2}-\d{2}\b',         # Matches dates in YYYY-MM-DD format
    r'\b\w{3,9} \d{1,2}, \d{4}\b'     # Matches dates in "Month day, year" format (e.g., Sep 12, 2023 or October 1, 2023)
]

# Combine the regular expressions into a single pattern
combined_pattern = '|'.join(regex_patterns)

# Find all matches in the text
matches = re.findall(combined_pattern, text)

# Output the extracted dates
print("Extracted Dates:")
for match in matches:
    print(match)
