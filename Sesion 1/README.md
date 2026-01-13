# Agente de Service Desk con AWS Bedrock

Agente conversacional desarrollado con LangChain y AWS Bedrock (Claude) para asistencia de Service Desk.

## 🚀 Características

- Integración con AWS Bedrock usando Claude 3 Sonnet
- Interfaz conversacional interactiva
- Gestión segura de credenciales con variables de entorno
- Historial de conversación mantenido durante la sesión

## 📋 Requisitos

- Python 3.8+
- Credenciales de AWS con acceso a Bedrock
- Cuenta de AWS con permisos para usar modelos de Claude

## 🔧 Instalación

1. Clona el repositorio o descarga los archivos

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Configura las variables de entorno creando un archivo `.env`:
```env
AWS_ACCESS_KEY_ID=tu_access_key_id
AWS_SECRET_ACCESS_KEY=tu_secret_access_key
AWS_DEFAULT_REGION=us-east-1
```

O configura las variables de entorno del sistema:
```powershell
$env:AWS_ACCESS_KEY_ID="tu_access_key_id"
$env:AWS_SECRET_ACCESS_KEY="tu_secret_access_key"
$env:AWS_DEFAULT_REGION="us-east-1"
```

## ▶️ Uso

### Opción 1: Usando el script PowerShell
```powershell
.\ejecutar.ps1
```

### Opción 2: Usando el script Batch
```cmd
ejecutar.bat
```

### Opción 3: Ejecutar directamente
```bash
python agent.py
```

Una vez ejecutado, el agente estará listo para recibir preguntas. Escribe `salir` para terminar la conversación.

## 📝 Estructura del Proyecto

```
Sesion 1/
├── agent.py              # Script principal del agente
├── requirements.txt      # Dependencias del proyecto
├── .env                  # Variables de entorno (NO se sube al repositorio)
├── .env.example          # Plantilla de variables de entorno
├── .gitignore            # Archivos ignorados por Git
├── ejecutar.ps1          # Script de ejecución para PowerShell
├── ejecutar.bat          # Script de ejecución para CMD
└── README.md             # Este archivo
```

## 🔒 Seguridad

- **NUNCA** subas el archivo `.env` al repositorio
- El archivo `.env` está protegido por `.gitignore`
- Usa `.env.example` como plantilla para compartir la estructura

## 🛠️ Tecnologías Utilizadas

- **LangChain**: Framework para aplicaciones con LLMs
- **LangChain AWS**: Integración con AWS Bedrock
- **Boto3**: SDK de AWS para Python
- **python-dotenv**: Gestión de variables de entorno

## 📚 Modelos Disponibles

El código está configurado para usar `anthropic.claude-3-sonnet-20240229-v1:0` por defecto.

Otras opciones compatibles con on-demand:
- `anthropic.claude-3-haiku-20240307-v1:0` (más rápido y económico)
- `anthropic.claude-3-opus-20240229-v1:0` (más potente, requiere inference profile)

## 📄 Licencia

Este proyecto es parte de un curso educativo.

## 👤 Autor

Jefferson Quispe

