import os
import requests

def main():
    api_key = os.environ['GROQ_API_KEY']
    print("Groq Quickstart Conversational Chatbot")
    print("A simple application that allows users to interact with a conversational chatbot powered by Groq.")
    print("This application is designed to get users up and running quickly with building a chatbot.")
    print("")
    print("Features:")
    print("Conversational Interface: Provides a simple interface where users can input text and receive responses from the chatbot.")
    print("Short Responses: The chatbot replies with very short and concise answers, keeping interactions brief and to the point.")
    print("Groq Integration: Utilizes the Groq API to generate responses, leveraging the power of the Llama3-70b-8192 model.")
    print("")
    print("Usage:")
    print("You will need to store a valid Groq API Key as a secret to proceed with this example.")
    print("You can generate one for free here.")
    print("You can fork and run this application on Replit or run it on the command line with python main.py.")
    
    while True:
        user_input = input("You: ")
        response = requests.post(f"https://api.groq.com/v1/llama/{api_key}", json={"prompt": user_input}).json()
        print(f"Chatbot: {response['response']}")
    input("Press Enter to exit...")
