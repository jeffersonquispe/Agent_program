import os
import json
from pathlib import Path
from dotenv import load_dotenv
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage, SystemMessage

# Constantes
PROMPTS_DIR = Path(__file__).parent / "prompts"
CONFIG_FILE = PROMPTS_DIR / "prompts_config.json"

def load_prompts_config():
    """Carga la configuración de prompts desde el archivo JSON"""
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo de configuración: {CONFIG_FILE}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error al parsear el archivo de configuración: {e}")

def list_available_prompts(config):
    """Lista todos los prompts disponibles con información sobre técnicas"""
    prompts = config.get("prompts", {})
    print("\n" + "="*70)
    print("TÉCNICAS DE PROMPT ENGINEERING DISPONIBLES")
    print("="*70)
    for key, info in prompts.items():
        technique = info.get('technique', 'N/A')
        description = info.get('description', 'Sin descripción')
        use_case = info.get('use_case', 'N/A')
        version = info.get('version', 'N/A')
        print(f"\n🔹 {key.upper()}")
        print(f"   Técnica: {technique}")
        print(f"   Descripción: {description}")
        print(f"   Mejor para: {use_case}")
        print(f"   Versión: {version}")
    print("\n" + "="*70 + "\n")

def load_prompt(prompt_key, config):
    """Carga el contenido de un prompt específico"""
    prompts = config.get("prompts", {})
    
    if prompt_key not in prompts:
        raise ValueError(f"Prompt '{prompt_key}' no encontrado en la configuración")
    
    prompt_info = prompts[prompt_key]
    prompt_file = PROMPTS_DIR / prompt_info["file"]
    
    try:
        with open(prompt_file, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo de prompt: {prompt_file}")

def select_prompt(config):
    """Permite al usuario seleccionar un prompt"""
    list_available_prompts(config)
    
    default_prompt = config.get("default", "zero_shot")
    prompt_key = input(f"Selecciona una técnica de prompt (Enter para usar '{default_prompt}'): ").strip()
    
    if not prompt_key:
        prompt_key = default_prompt
    
    if prompt_key not in config.get("prompts", {}):
        print(f"⚠️  Prompt '{prompt_key}' no válido. Usando '{default_prompt}' por defecto.")
        prompt_key = default_prompt
    
    return prompt_key

def main():
    print("=== Agente de Service Desk con Versionamiento de Prompts ===")
    print("Escribe 'salir' para terminar, 'cambiar' para cambiar de prompt, 'listar' para ver prompts\n")

    # Carga las variables de entorno desde el archivo .env
    load_dotenv()

    # Obtiene las credenciales AWS desde variables de entorno
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    aws_region = os.getenv("AWS_DEFAULT_REGION", "us-east-1")

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

    # Carga la configuración de prompts
    config = load_prompts_config()
    
    # Permite al usuario seleccionar un prompt inicial
    current_prompt_key = select_prompt(config)
    current_prompt = load_prompt(current_prompt_key, config)
    
    print(f"\n✅ Técnica activa: {current_prompt_key.upper()}")
    prompts_info = config.get("prompts", {}).get(current_prompt_key, {})
    print(f"📚 Técnica: {prompts_info.get('technique', 'N/A')}")
    print(f"📋 Descripción: {prompts_info.get('description', 'Sin descripción')}")
    print(f"🎯 Mejor para: {prompts_info.get('use_case', 'N/A')}\n")

    # Inicializa el modelo de Bedrock
    llm = ChatBedrock(
        model_id="anthropic.claude-3-sonnet-20240229-v1:0",
        region_name=aws_region
    )
    
    # Inicializa el historial con el mensaje del sistema (prompt)
    historial = [SystemMessage(content=current_prompt)]

    while True:
        pregunta = input("Tú: ")
        
        if pregunta.lower() == 'salir':
            print("Agente: ¡Hasta luego!")
            break
        
        if pregunta.lower() == 'cambiar':
            try:
                new_prompt_key = select_prompt(config)
                current_prompt = load_prompt(new_prompt_key, config)
                current_prompt_key = new_prompt_key
                
                # Reinicia el historial con el nuevo prompt del sistema
                historial = [SystemMessage(content=current_prompt)]
                
                prompts_info = config.get("prompts", {}).get(current_prompt_key, {})
                print(f"\n✅ Técnica cambiada a: {current_prompt_key.upper()}")
                print(f"📚 Técnica: {prompts_info.get('technique', 'N/A')}")
                print(f"📋 Descripción: {prompts_info.get('description', 'Sin descripción')}")
                print(f"🎯 Mejor para: {prompts_info.get('use_case', 'N/A')}\n")
            except Exception as e:
                print(f"❌ Error al cambiar el prompt: {e}\n")
            continue
        
        if pregunta.lower() == 'listar':
            list_available_prompts(config)
            continue
        
        # Agrega la pregunta del usuario al historial
        historial.append(HumanMessage(content=pregunta))
        
        try:
            respuesta = llm.invoke(historial)
            print(f"Agente: {respuesta.content}\n")
            historial.append(respuesta)
        except Exception as e:
            print(f"❌ Se produjo un error al consultar el modelo: {e}\n")

if __name__ == "__main__":
    main()
