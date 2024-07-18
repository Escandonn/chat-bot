# Chatbot Conversacional con Groq y LangChain

## Descripción

Esta aplicación es un chatbot conversacional impulsado por LangChain y la API de Groq. Permite a los usuarios interactuar con el chatbot, que puede responder preguntas, proporcionar información o simplemente charlar. El chatbot mantiene un historial de la conversación para proporcionar contexto en sus respuestas.

## Requisitos

- Python 3.x
- Una clave API de Groq

## Instalación

1. Clona este repositorio:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_DIRECTORIO>
    ```

2. Instala las dependencias necesarias:
    ```sh
    pip install groq langchain
    ```

3. Configura tu clave de API de Groq en el código:
    ```python
    os.environ['GROQ_API_KEY'] = "TU_CLAVE_API_DE_GROQ"
    ```

## Uso

1. Ejecuta el script principal:
    ```sh
    python main.py
    ```

2. Ingresa tus preguntas cuando se te solicite y el chatbot responderá.

## Estructura del Código

- `main()`: La función principal que configura el cliente de Groq, la interfaz y maneja la interacción del chat.
- `system_prompt`: Define el comportamiento del chatbot.
- `ConversationBufferWindowMemory`: Objeto de memoria que almacena y gestiona el historial de la conversación.
- `ChatPromptTemplate`: Construye una plantilla de chat utilizando varios componentes.



