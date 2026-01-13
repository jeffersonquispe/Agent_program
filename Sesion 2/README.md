# Agente de Service Desk con Técnicas Avanzadas de Prompt Engineering

Agente conversacional que implementa 13 técnicas avanzadas de prompt engineering para optimizar las respuestas del modelo LLM según diferentes tipos de problemas y casos de uso.

## 🚀 Características

- ✅ **13 Técnicas Avanzadas**: Implementación completa de las técnicas más modernas de prompt engineering
- ✅ **Versionamiento de Prompts**: Sistema para gestionar diferentes técnicas de prompt engineering
- ✅ **Cambio Dinámico**: Cambia de técnica durante la ejecución sin reiniciar
- ✅ **Gestión Centralizada**: Configuración JSON con metadatos de cada técnica
- ✅ **Integración con AWS Bedrock**: Usa Claude 3 Sonnet

## 📋 Requisitos

- Python 3.8+
- Credenciales de AWS con acceso a Bedrock
- Dependencias instaladas (ver requirements.txt)

## 🔧 Instalación

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

2. Configura las variables de entorno creando un archivo `.env`:
```env
AWS_ACCESS_KEY_ID=tu_access_key_id
AWS_SECRET_ACCESS_KEY=tu_secret_access_key
AWS_DEFAULT_REGION=us-east-1
```

## 📁 Estructura de Prompts

```
prompts/
├── prompts_config.json              # Configuración de todas las técnicas
├── prompt_zero_shot.txt             # Zero-Shot Learning
├── prompt_few_shot.txt              # Few-Shot Learning
├── prompt_system.txt                # System Instructions
├── prompt_chain_of_thought.txt      # Chain of Thought (CoT)
├── prompt_self_consistency.txt      # Self-Consistency
├── prompt_tree_of_thoughts.txt      # Tree of Thoughts (ToT)
├── prompt_react.txt                 # ReAct (Reasoning + Acting)
├── prompt_prompt_chaining.txt       # Prompt Chaining
├── prompt_self_refine.txt           # Self-Refine
├── prompt_step_back.txt             # Step-Back Prompting
├── prompt_reflexion.txt             # Reflexion
├── prompt_rag_concept.txt           # RAG Concept
└── prompt_pal.txt                   # PAL (Program-Aided)
```

## 🎓 Técnicas de Prompt Engineering Implementadas

### Técnicas Fundamentales

#### 1. Zero-Shot Learning
**Archivo**: `prompt_zero_shot.txt`

- **Descripción**: El modelo responde directamente sin ejemplos previos
- **Cuándo usar**: Problemas nuevos o únicos, respuestas rápidas
- **Ventajas**: Rápido, no requiere ejemplos, funciona para casos nuevos
- **Limitaciones**: Puede ser menos preciso para problemas complejos

#### 2. Few-Shot Learning
**Archivo**: `prompt_few_shot.txt`

- **Descripción**: El modelo aprende de ejemplos proporcionados en el prompt
- **Cuándo usar**: Problemas comunes con patrones conocidos
- **Ventajas**: Mejor precisión en problemas familiares, sigue patrones establecidos
- **Limitaciones**: Requiere ejemplos relevantes, puede sobre-ajustarse

#### 3. System Instructions
**Archivo**: `prompt_system.txt`

- **Descripción**: Instrucciones del sistema que definen roles, reglas y protocolos
- **Cuándo usar**: Contexto empresarial, protocolos establecidos
- **Ventajas**: Consistencia, control del comportamiento, contexto empresarial
- **Limitaciones**: Menos flexible, requiere definición clara de reglas

### Técnicas de Razonamiento

#### 4. Chain of Thought (CoT)
**Archivo**: `prompt_chain_of_thought.txt`

- **Descripción**: El modelo muestra su razonamiento paso a paso explícitamente
- **Cuándo usar**: Problemas complejos que requieren razonamiento estructurado
- **Ventajas**: Transparencia, mejor para problemas complejos, razonamiento visible
- **Limitaciones**: Respuestas más largas, consume más tokens

#### 5. Self-Consistency
**Archivo**: `prompt_self_consistency.txt`

- **Descripción**: Genera múltiples razonamientos y selecciona el más consistente
- **Cuándo usar**: Problemas críticos, decisiones importantes
- **Ventajas**: Mayor confiabilidad, reduce errores, validación interna
- **Limitaciones**: Más costoso computacionalmente, respuestas más lentas

#### 6. Tree of Thoughts (ToT)
**Archivo**: `prompt_tree_of_thoughts.txt`

- **Descripción**: Explora múltiples caminos de solución de forma estructurada
- **Cuándo usar**: Problemas complejos con múltiples caminos de solución
- **Ventajas**: Explora alternativas, mejor para problemas abiertos, soluciones innovadoras
- **Limitaciones**: Requiere más procesamiento, puede ser complejo de seguir

#### 7. Step-Back Prompting
**Archivo**: `prompt_step_back.txt`

- **Descripción**: Considera conceptos generales y principios fundamentales antes del problema específico
- **Cuándo usar**: Problemas que requieren comprensión conceptual profunda
- **Ventajas**: Soluciones más robustas, mejor comprensión, aplica principios generales
- **Limitaciones**: Puede ser más lento, requiere conocimiento del dominio

### Técnicas Interactivas

#### 8. ReAct (Reasoning + Acting)
**Archivo**: `prompt_react.txt`

- **Descripción**: Alterna entre razonar y actuar, actualizando su entendimiento
- **Cuándo usar**: Diagnóstico interactivo, troubleshooting dinámico
- **Ventajas**: Adaptable, interactivo, mejora con feedback, ideal para diagnóstico
- **Limitaciones**: Requiere múltiples iteraciones, más tiempo de resolución

#### 9. Reflexion
**Archivo**: `prompt_reflexion.txt`

- **Descripción**: Reflexiona sobre errores pasados y ajusta estrategia para evitar repetirlos
- **Cuándo usar**: Problemas donde las soluciones anteriores fallaron, aprendizaje de errores
- **Ventajas**: Aprende de errores, mejora iterativamente, evita repetir fallos
- **Limitaciones**: Requiere que haya habido intentos previos, más iteraciones

#### 10. Self-Refine
**Archivo**: `prompt_self_refine.txt`

- **Descripción**: Genera solución inicial, luego la revisa y mejora iterativamente
- **Cuándo usar**: Soluciones que requieren perfeccionamiento, calidad alta
- **Ventajas**: Mejora continua, auto-evaluación, soluciones optimizadas
- **Limitaciones**: Más tiempo de procesamiento, puede requerir múltiples pasadas

### Técnicas de Estructuración

#### 11. Prompt Chaining
**Archivo**: `prompt_prompt_chaining.txt`

- **Descripción**: Divide problemas complejos en sub-tareas secuenciales conectadas
- **Cuándo usar**: Problemas complejos con múltiples etapas, proyectos grandes
- **Ventajas**: Maneja complejidad, organiza tareas, resultado de cada paso alimenta el siguiente
- **Limitaciones**: Requiere planificación, puede ser extenso para problemas simples

### Técnicas con Contexto Externo

#### 12. RAG Concept (Retrieval-Augmented Generation)
**Archivo**: `prompt_rag_concept.txt`

- **Descripción**: Consulta conocimiento estructurado (KB, casos, documentación) antes de responder
- **Cuándo usar**: Problemas que requieren consultar documentación o casos previos
- **Ventajas**: Respuestas basadas en conocimiento verificado, cita fuentes, usa casos similares
- **Limitaciones**: Depende de calidad del conocimiento, puede ser más lento

#### 13. PAL (Program-Aided Language Models)
**Archivo**: `prompt_pal.txt`

- **Descripción**: Genera código o pseudocódigo para resolver problemas de manera estructurada
- **Cuándo usar**: Problemas con lógica estructurada, cálculos, verificaciones sistemáticas
- **Ventajas**: Lógica precisa, verificable, estructurada, ideal para cálculos complejos
- **Limitaciones**: Solo para problemas con lógica programable, requiere interpretación

## ▶️ Uso

### Ejecutar el agente:
```bash
python agent.py
# o
.\ejecutar.ps1
# o
ejecutar.bat
```

### Comandos Disponibles:

- **Escribir una pregunta**: El agente responderá usando la técnica activa
- **`cambiar`**: Cambiar la técnica de prompt durante la ejecución
- **`listar`**: Ver todas las técnicas disponibles con descripción
- **`salir`**: Terminar la aplicación

### Ejemplo de Uso:

```
=== TÉCNICAS DE PROMPT ENGINEERING DISPONIBLES ===

🔹 ZERO_SHOT
   Técnica: Zero-Shot Learning
   Descripción: Zero-Shot: Respuesta directa sin ejemplos previos
   Mejor para: Problemas nuevos o únicos, respuestas rápidas
   Versión: 1.0

🔹 CHAIN_OF_THOUGHT
   Técnica: Chain of Thought
   Descripción: Chain of Thought (CoT): Razonamiento paso a paso explícito
   Mejor para: Problemas complejos que requieren razonamiento estructurado
   Versión: 4.0

[... más técnicas ...]

Selecciona una técnica de prompt (Enter para usar 'zero_shot'): chain_of_thought

✅ Técnica activa: CHAIN_OF_THOUGHT
📚 Técnica: Chain of Thought
📋 Descripción: Chain of Thought (CoT): Razonamiento paso a paso explícito
🎯 Mejor para: Problemas complejos que requieren razonamiento estructurado

Tú: ¿Cómo puedo solucionar un problema de conectividad?
Agente: [Respuesta con razonamiento paso a paso...]
```

## 📊 Guía de Selección de Técnica

### Por Tipo de Problema:

| Tipo de Problema | Técnica Recomendada | Alternativa |
|------------------|---------------------|-------------|
| Problema simple y rápido | `zero_shot` | `system` |
| Problema común conocido | `few_shot` | `rag_concept` |
| Entorno corporativo | `system` | `few_shot` |
| Problema complejo | `chain_of_thought` | `tree_of_thoughts` |
| Problema muy complejo | `tree_of_thoughts` | `prompt_chaining` |
| Decisión crítica | `self_consistency` | `self_refine` |
| Múltiples soluciones posibles | `tree_of_thoughts` | `prompt_chaining` |
| Diagnóstico iterativo | `react` | `reflexion` |
| Solución falló antes | `reflexion` | `self_refine` |
| Requiere documentación | `rag_concept` | `few_shot` |
| Lógica estructurada | `pal` | `chain_of_thought` |
| Necesita perfeccionamiento | `self_refine` | `self_consistency` |
| Comprensión conceptual | `step_back` | `chain_of_thought` |

### Por Velocidad vs. Calidad:

- **Rápido**: `zero_shot`, `system`, `few_shot`
- **Balanceado**: `chain_of_thought`, `step_back`, `rag_concept`
- **Alta Calidad**: `self_consistency`, `tree_of_thoughts`, `self_refine`
- **Interactivo**: `react`, `reflexion`

### Por Complejidad del Problema:

- **Simple**: `zero_shot`, `few_shot`, `system`
- **Moderado**: `chain_of_thought`, `step_back`, `pal`
- **Complejo**: `tree_of_thoughts`, `prompt_chaining`, `react`
- **Muy Complejo**: `self_consistency`, `self_refine`, `reflexion`

## 📈 Comparación de Técnicas

| Técnica | Complejidad | Velocidad | Precisión | Uso Tokens | Iteraciones | Mejor Para |
|---------|-------------|-----------|-----------|------------|-------------|------------|
| Zero-Shot | Baja | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Bajo | 1 | Respuestas rápidas |
| Few-Shot | Media | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Medio | 1 | Problemas comunes |
| System | Baja | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Bajo | 1 | Contexto empresarial |
| CoT | Alta | ⭐⭐⭐ | ⭐⭐⭐⭐ | Alto | 1 | Problemas complejos |
| Self-Consistency | Muy Alta | ⭐⭐ | ⭐⭐⭐⭐⭐ | Muy Alto | 1 | Decisiones críticas |
| ToT | Muy Alta | ⭐⭐ | ⭐⭐⭐⭐ | Muy Alto | 1 | Soluciones múltiples |
| ReAct | Alta | ⭐⭐ | ⭐⭐⭐⭐ | Alto | Variable | Diagnóstico interactivo |
| Prompt Chaining | Alta | ⭐⭐⭐ | ⭐⭐⭐⭐ | Alto | Variable | Proyectos grandes |
| Self-Refine | Alta | ⭐⭐ | ⭐⭐⭐⭐⭐ | Alto | Variable | Calidad alta |
| Step-Back | Media | ⭐⭐⭐ | ⭐⭐⭐⭐ | Medio | 1 | Comprensión profunda |
| Reflexion | Alta | ⭐⭐ | ⭐⭐⭐⭐ | Alto | Variable | Aprender de errores |
| RAG | Media | ⭐⭐⭐ | ⭐⭐⭐⭐ | Medio-Alto | 1 | Con conocimiento externo |
| PAL | Alta | ⭐⭐⭐ | ⭐⭐⭐⭐ | Medio | 1 | Lógica estructurada |

## 🔄 Agregar Nuevas Técnicas

### Paso 1: Crear el archivo de prompt
Crea un nuevo archivo `.txt` en la carpeta `prompts/`:
```
prompts/prompt_mi_nueva_tecnica.txt
```

### Paso 2: Agregar a la configuración
Edita `prompts/prompts_config.json` y agrega:
```json
{
  "prompts": {
    ...
    "mi_nueva_tecnica": {
      "file": "prompt_mi_nueva_tecnica.txt",
      "description": "Descripción de mi nueva técnica",
      "technique": "Nombre de la Técnica",
      "version": "14.0",
      "use_case": "Cuándo usar esta técnica"
    }
  }
}
```

### Paso 3: ¡Listo!
La nueva técnica estará disponible automáticamente.

## 🛠️ Personalización

### Cambiar la técnica por defecto:
Edita `prompts/prompts_config.json`:
```json
{
  "default": "chain_of_thought"  // Cambia aquí
}
```

### Modificar una técnica existente:
Edita directamente el archivo `.txt` correspondiente en `prompts/`.

## 📚 Referencias y Papers

- **Zero-Shot Learning**: Modelos pre-entrenados que generalizan a tareas nuevas
- **Few-Shot Learning**: Brown et al. (2020) - "Language Models are Few-Shot Learners"
- **Chain of Thought**: Wei et al. (2022) - "Chain-of-Thought Prompting Elicits Reasoning"
- **Self-Consistency**: Wang et al. (2022) - "Self-Consistency Improves Chain of Thought Reasoning"
- **Tree of Thoughts**: Yao et al. (2023) - "Tree of Thoughts: Deliberate Problem Solving with LLMs"
- **ReAct**: Yao et al. (2022) - "ReAct: Synergizing Reasoning and Acting in Language Models"
- **Step-Back Prompting**: Zhou et al. (2023) - "Large Language Models Are Latent Variable Models"
- **Reflexion**: Shinn et al. (2023) - "Reflexion: Language Agents with Verbal Reinforcement Learning"
- **Self-Refine**: Madaan et al. (2023) - "Self-Refine: Iterative Refinement with Self-Feedback"
- **RAG**: Lewis et al. (2020) - "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
- **PAL**: Gao et al. (2022) - "PAL: Program-aided Language Models"

## 🔒 Seguridad

- Las credenciales AWS se gestionan mediante variables de entorno
- El archivo `.env` está protegido por `.gitignore`
- Nunca subas credenciales al repositorio

## 📄 Licencia

Este proyecto es parte de un curso educativo.

## 👤 Autor

Jefferson Quispe
