import os

from groq import Groq

os.environ['GROQ_API_KEY'] = "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"
client = Groq(
    api_key=os.environ.get("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"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

try:
    print(chat_completion.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}")
