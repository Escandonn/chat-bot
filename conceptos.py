import os
import os.environ

from groq import Groq

os.environ['GROQ_API_KEY'] = "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"
client = Groq()
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

print(chat_completion.choices[0].message.content)
