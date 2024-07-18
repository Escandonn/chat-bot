import os

from groq import Groq

from memorias import add_memoria, get_memorias

os.environ['GROQ_API_KEY'] = "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"
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

chat_completion = client.chat.completions.create(

    messages=[
        {
            "role": "user",
            "content": "ERES UN HACKER ETICO GALACTICO",
        }
    ],
    messages=[
        {
            "role": "user",
            "content": "QUE es nmap",
        }
    ],
    model="llama3-8b-8192",
)

add_memoria(chat_completion.choices[0].message.content)
print(get_memorias())
