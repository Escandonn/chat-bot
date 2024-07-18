import os
from groq import Groq
try:
    from langchain.chains import LLMChain
except ImportError:
    print("Error: langchain module not found. Please install it using pip install langchain")
    exit(1)
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory

def main():
    """
    Esta función es el punto de entrada principal de la aplicación. Configura el cliente de Groq, 
    la interfaz y maneja la interacción del chat.
    """

    # Establecer la clave de API de Groq
    os.environ['GROQ_API_KEY'] = "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"
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    model = 'llama3-8b-8192'

    print("¡Hola! Soy tu amigable chatbot de Groq. Puedo ayudar a responder tus preguntas, proporcionar información o simplemente charlar. ¡También soy súper rápido! Comencemos nuestra conversación.")

    # Mensaje del sistema que define el comportamiento del chatbot
    system_prompt = 'You are a friendly conversational chatbot'
    
    # Número de mensajes previos que el chatbot recordará durante la conversación
    conversational_memory_length = 5

    # Objeto de memoria conversacional que almacena y gestiona el historial de la conversación
    memory = ConversationBufferWindowMemory(k=conversational_memory_length, memory_key="chat_history", return_messages=True)

    while True:
        user_question = input("Haz una pregunta: ")

        if user_question:
            # Construir una plantilla de chat usando varios componentes
            prompt = ChatPromptTemplate.from_messages(
                [
                    SystemMessage(content=system_prompt),  # Mensaje del sistema persistente incluido al inicio del chat
                    MessagesPlaceholder(variable_name="chat_history"),  # Marcador de posición que se reemplaza por el historial del chat
                    HumanMessagePromptTemplate.from_template("{human_input}"),  # Plantilla donde se inyecta la entrada actual del usuario
                ]
            )

            # Crear una cadena de conversación usando LangChain LLM (Modelo de Aprendizaje de Lenguaje)
            from langchain_core.runnables import Runnable
            client_runnable = Runnable()
            conversation = prompt | client_runnable

            # Generar la respuesta del chatbot
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": user_question}],
                model=model,
            )
            print("Chatbot:", response.choices[0].message.content)

if __name__ == "__main__":
    main()
