import os

from groq import Groq
from bs4 import BeautifulSoup

os.environ['GROQ_API_KEY'] = "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"
client = Groq(
    api_key=os.environ.get("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"),
)

html_content = "<your_html_content_here>"  # replace with your HTML content
soup = BeautifulSoup(html_content, 'html.parser')
text = soup.get_text()
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

try:
    print(text)
except Exception as e:
    print(f"Error: {e}")
