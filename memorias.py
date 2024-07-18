import os
from groq import Groq

def set_environment(api_key):
    """
    Configura la variable de entorno necesaria para la autenticación de la API de Groq.

    Parámetros:
    api_key (str): La clave de API para autenticar con el servicio de Groq.
    """
    os.environ['GROQ_API_KEY'] = api_key

def create_groq_client():
    """
    Crea y devuelve un cliente Groq autenticado utilizando la clave de API configurada en el entorno.

    Retorna:
    Groq: Un objeto cliente de Groq autenticado.

    Lanza:
    ValueError: Si la clave de API no está configurada en el entorno.
    """
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY no está configurado en el entorno.")
    return Groq(api_key=api_key)

def get_chat_completion(client, model, messages):
    """
    Obtiene una respuesta del modelo de lenguaje basado en los mensajes proporcionados.

    Parámetros:
    client (Groq): El cliente autenticado de Groq.
    model (str): El nombre del modelo de lenguaje a utilizar.
    messages (list): Una lista de diccionarios que representan los mensajes en la conversación.

    Retorna:
    str: El contenido de la respuesta generada por el modelo de lenguaje.
    """
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
    )
    return chat_completion.choices[0].message.content

def main():
    """
    Función principal que coordina la configuración del entorno, la creación del cliente Groq,
    y la obtención de una respuesta del modelo de lenguaje. Imprime la respuesta obtenida.
    """
    # Configura la clave de API
    api_key = "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"
    set_environment(api_key)
    
    # Crea el cliente Groq
    client = create_groq_client()
    
    # Define los mensajes y el modelo de lenguaje a utilizar
    messages = [
        {
            "role": "user",
            "content": "Los numeros del 1 al 10 en español",
        }
    ]
    model = "llama3-8b-8192"
    
    # Obtiene la respuesta del modelo de lenguaje y la imprime
    response = get_chat_completion(client, model, messages)
    print(response)

# Ejecuta la función principal si este script es ejecutado directamente
if __name__ == "__main__":
    main()
