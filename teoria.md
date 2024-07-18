#set GROQ_API_KEY in the secrets

import os
from groq import Groq

# Create the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"), )

# Set the system prompt
system_prompt = {
    "role": "system",
    "content":
    "You are a helpful assistant. You reply with very short answers."
}

# Initialize the chat history
chat_history = [system_prompt]

while True:
  # Get user input from the console
  user_input = input("You: ")

  # Append the user input to the chat history
  chat_history.append({"role": "user", "content": user_input})

  response = client.chat.completions.create(model="llama3-70b-8192",
                                            messages=chat_history,
                                            max_tokens=100,
                                            temperature=1.2)
  # Append the response to the chat history
  chat_history.append({
      "role": "assistant",
      "content": response.choices[0].message.content
  })
  # Print the response
  print("Assistant:", response.choices[0].message.content)


Groq Quickstart Conversational Chatbot
A simple application that allows users to interact with a conversational chatbot powered by Groq. This application is designed to get users up and running quickly with building a chatbot.

Features
Conversational Interface: Provides a simple interface where users can input text and receive responses from the chatbot.

Short Responses: The chatbot replies with very short and concise answers, keeping interactions brief and to the point.

Groq Integration: Utilizes the Groq API to generate responses, leveraging the power of the Llama3-70b-8192 model.

Usage
You will need to store a valid Groq API Key as a secret to proceed with this example. You can generate one for free here.

You can fork and run this application on Replit or run it on the command line with python main.py.