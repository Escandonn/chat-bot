import os
from groq import Groq

# Establecer la clave de API de Groq como variable de entorno
os.environ['GROQ_API_KEY'] = ""

# Crear un cliente Groq con la clave de API establecida
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Iniciar la conversación
conversation = []

while True:
    user_input = input("User: ")
    print(user_input)
    if user_input == "cero":
        break
    
    # Guardar la pregunta del usuario en la conversación
    conversation.append(f"User: {user_input}")

    # Enviar la pregunta al modelo de Groq
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="llama3-8b-8192",
    )

    # Obtener y guardar la respuesta del asistente
    assistant_response = chat_completion.choices[0].message.content.strip()
    conversation.append(f"Assistant: {assistant_response}")

    # Imprimir la respuesta del asistente
    print(f"Assistant: {assistant_response}")

# Imprimir toda la conversación al salir del bucle
print("\n--- Conversación completa ---")
for utterance in conversation:
    print(utterance)
