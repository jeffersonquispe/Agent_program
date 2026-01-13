import os
from dotenv import load_dotenv
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage

def main():
    print("Agente de Service Desk (escribe 'salir' para terminar)")

    # Carga las variables de entorno desde el archivo .env
    load_dotenv()

    # Obtiene las credenciales AWS desde variables de entorno
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    aws_region = os.getenv("AWS_DEFAULT_REGION", "us-east-1")  # Valor por defecto si no está definido

    # Valida que las credenciales estén configuradas
    if not aws_access_key_id or not aws_secret_access_key:
        raise ValueError(
            "Error: Las credenciales AWS no están configuradas. "
            "Por favor, configura las variables de entorno AWS_ACCESS_KEY_ID y AWS_SECRET_ACCESS_KEY, "
            "o crea un archivo .env con estas variables."
        )

    # Establece las variables de entorno requeridas por boto3/AWS SDK
    os.environ["AWS_ACCESS_KEY_ID"] = aws_access_key_id
    os.environ["AWS_SECRET_ACCESS_KEY"] = aws_secret_access_key
    os.environ["AWS_DEFAULT_REGION"] = aws_region

    # Inicializa el modelo de Bedrock
    # Modelos disponibles con on-demand: anthropic.claude-3-sonnet-20240229-v1:0, anthropic.claude-3-haiku-20240307-v1:0
    llm = ChatBedrock(
        model_id="anthropic.claude-3-sonnet-20240229-v1:0",  # Claude 3 Sonnet - compatible con on-demand
        region_name=aws_region
    )
    historial = []
    while True:
        pregunta = input("Tú: ")
        if pregunta.lower() == 'salir':
            print("Agente: ¡Hasta luego!")
            break
        historial.append(HumanMessage(content=pregunta))
        try:
            respuesta = llm.invoke(historial)
            print(f"Agente: {respuesta.content}")
            historial.append(respuesta)
        except Exception as e:
            print(f"Se produjo un error al consultar el modelo: {e}")

if __name__ == "__main__":
    main()

"""
Cómo ejecutar este código en el IDE Cursor en Windows 11:

1. Abre el archivo 'agent.py' en Cursor.

2. Instala las dependencias ejecutando:
   pip install -r requirements.txt

3. Configura las variables de entorno:
   
   Opción A: Crea un archivo .env en la misma carpeta con el siguiente contenido:
   AWS_ACCESS_KEY_ID=tu_access_key_id
   AWS_SECRET_ACCESS_KEY=tu_secret_access_key
   AWS_DEFAULT_REGION=us-east-1
   
   Opción B: Configura las variables de entorno del sistema:
   - En Windows PowerShell:
     $env:AWS_ACCESS_KEY_ID="tu_access_key_id"
     $env:AWS_SECRET_ACCESS_KEY="tu_secret_access_key"
     $env:AWS_DEFAULT_REGION="us-east-1"

4. Una vez configuradas las credenciales, ejecuta el script usando:
   python agent.py

El agente te pedirá preguntas; escribe tu consulta y presiona Enter.
Escribe 'salir' para terminar la conversación.

Nota: Para mayor seguridad, usa variables de entorno y no hardcodees las credenciales en el código.
¡Listo! Así puedes usar el agente desde Cursor en Windows 11 de manera sencilla.
"""

