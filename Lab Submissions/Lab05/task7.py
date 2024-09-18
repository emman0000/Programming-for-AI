
import re

def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails

text = """
My personal email address is areeba.hasnain@gmail.com
My FAST email address is k230059@nu.edu.pk
"""

emails = extract_emails(text)
print("Extracted email addresses:")
for email in emails:
    print(email)
