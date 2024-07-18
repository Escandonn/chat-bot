import os
# Importación del módulo os para interactuar con el entorno del sistema

from groq import Groq
# Importación del cliente Groq para interactuar con la API de Groq
from bs4 import BeautifulSoup
# Importación de la biblioteca BeautifulSoup para parsear HTML

os.environ['GROQ_API_KEY'] = "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"
# Establecer la clave de API de Groq como variable de entorno
client = Groq(
    api_key=os.environ.get("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"),
)
# Crear un cliente Groq con la clave de API establecida

html_content = "<your_html_content_here>"  # reemplazar con su contenido HTML
# Contenido HTML que se va a parsear
soup = BeautifulSoup(html_content, 'html.parser')
# Parsear el contenido HTML con BeautifulSoup
text = soup.get_text()
# Extraer el texto del contenido HTML parseado

try:
    print(text)
except Exception as e:
    print(f"Error: {e}")
# Intentar imprimir el texto extraído, y capturar cualquier error que ocurra
