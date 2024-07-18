# Groq Quickstart Conversational Chatbot Tutorial
=====================================================

This tutorial will guide you through creating a simple conversational chatbot powered by Groq.

## Prerequisites
----------------

* A valid Groq API Key (you can generate one for free [here](https://groq.com/))
* Python installed on your system
* The `groq` library installed (you can install it using `pip install groq`)

## Setting up the Environment
-----------------------------

### 1. Set up your Groq API Key

Create a new file `memorias.py` and add the following code:
```python
import os
from groq import Groq

def set_environment(api_key):
    os.environ['GROQ_API_KEY'] = api_key

# Replace with your own API Key
api_key = "YOUR_API_KEY"
set_environment(api_key)
```
### 2. Create a Groq Client

Add the following code to `memorias.py`:
```python
def create_groq_client():
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not set in the environment.")
    return Groq(api_key=api_key)

client = create_groq_client()
```
## Creating the Chatbot
---------------------

### 1. Define the Conversation

Create a new file `new_file.py` and add the following code:
```python
import os
from groq import Groq

# Initialize the conversation
conversation = []

while True:
    user_input = input("User: ")
    print(user_input)
    if user_input == "cero":
        break
    
    # Save the user's question to the conversation
    conversation.append(f"User: {user_input}")

    # Send the question to the Groq model
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="llama3-8b-8192",
    )

    # Get and save the assistant's response
    assistant_response = chat_completion.choices[0].message.content.strip()
    conversation.append(f"Assistant: {assistant_response}")

    # Print the assistant's response
    print(f"Assistant: {assistant_response}")

# Print the entire conversation when exiting the loop
print("\n--- Conversation Complete ---")
for utterance in conversation:
    print(utterance)
```
### 2. Run the Chatbot

Run the chatbot using `python new_file.py`. You can interact with the chatbot by inputting text, and it will respond accordingly.

## Conclusion
----------

Congratulations! You have successfully created a simple conversational chatbot powered by Groq. You can now experiment with different models and fine-tune the chatbot to suit your needs.
