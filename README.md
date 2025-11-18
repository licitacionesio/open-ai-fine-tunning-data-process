# Open AI Fine-Tunning Data Process

## Acerca del proyecto
**Open AI Fine-Tunning Data Process** es una herramienta desarrollada por [Licitaciones.io](https://licitaciones.io) diseñada para facilitar el preprocesamiento de datos textuales necesarios para entrenar modelos de inteligencia artificial mediante fine-tuning en la plataforma OpenAI API.  
Su propósito es convertir datos brutos —como texto libre, preguntas-respuestas o registros de usuario— en archivos `.jsonl` correctamente formateados y listos para el entrenamiento.

Este proyecto acompaña al artículo formativo publicado en Medium: *[Modelo de clasificación personalizado con OpenAI](https://medium.com/@contact_6663/modelo-de-clasificaci%C3%B3n-personalizado-con-openai-56d4335023d2)*

---

## ¿Por qué es útil?
El *fine-tuning* permite adaptar un modelo genérico a un dominio específico (jurídico, sanitario, financiero, educativo, etc.).  
El principal desafío suele ser la preparación de datos: limpieza, estructura y conversión al formato requerido por OpenAI.  
Este proyecto resuelve ese punto crítico al automatizar la transformación hacia el formato `.jsonl`.

Incluye:
- Conversión rápida de datos textuales a JSONL
- Código Python, fácilmente integrable en cualquier proyecto
- Dependencias mínimas y estructura clara

---

## Características principales
- **Transformación automática a `.jsonl`** siguiendo el formato necesario para `prompt` y `completion`.
- **Estructura modular** con carpetas como `data/`, `helpers/` y un `main.py` fácil de adaptar.
- **Instrucciones de instalación** mediante `pip install -r requirements.txt`.
- **Compatibilidad total** con flujos de trabajo destinados al fine-tuning con OpenAI.

---

## Beneficios para tus proyectos de IA
- **Ahorro de tiempo:** evita el formateo manual y reduce errores.
- **Menos barreras técnicas:** útil tanto para desarrolladores como para equipos no especializados.
- **Mayor calidad del dataset:** un formato bien preparado mejora los resultados del modelo.
- **Flexibilidad absoluta:** se adapta a múltiples sectores y tipos de datos.

---

## Casos de uso
- Entrenamiento de modelos especializados para clasificar documentos públicos o administrativos.
- Creación de asistentes virtuales con conocimiento profundo en un área concreta.
- Automatización de la preparación de datasets en consultoras y proyectos de innovación.
- Preparación de datos para análisis de sentimiento, clasificación o generación de texto.

---

## Cómo empezar

### 1. Clona el repositorio
```bash
git clone https://github.com/licitacionesio/open-ai-fine-tunning-data-process.git
```

### 2. Instala las dependencias
```bash
pip install -r requirements.txt
```

### 3. Prepara tus datos
Coloca tu fichero de datos (texto, CSV, JSON o similar) en el directorio data/.

### 4. Ejecuta el script principal
```bash
python main.py
```

### 5. Obtén el resultado
El archivo de salida .jsonl estará listo para subirlo a OpenAI e iniciar el proceso de fine-tuning.

### Futuras mejoras
- CLI mejorado con parámetros configurables.
- Compatibilidad con formatos de entrada adicionales (CSV, Excel, SQL).
- Validación automática del .jsonl según requisitos de OpenAI.
- Integración con flujos de datos en la nube (S3, GCS).
- Reportes automáticos de calidad del dataset.

### Contribuciones
Las contribuciones son bienvenidas.
Si deseas mejorar la herramienta, abrir un issue o proponer nuevas funcionalidades, siéntete libre de colaborar mediante pull requests.

### Relación con Licitaciones.io
Este proyecto forma parte de las iniciativas abiertas de [Licitaciones.io](https://licitaciones.io), una plataforma especializada en inteligencia artificial aplicada al análisis automatizado de licitaciones públicas en España.

### Licencia
Consulta el archivo LICENSE para más información sobre los términos de uso y redistribución.
