# Proyecto Final – Pipeline de Datos (Semana 3)

## Descripción
Este proyecto corresponde al **Mes 3 del curso de Análisis de Datos**, enfocado en **Herramientas ETL y un Proyecto Final**.  
Durante esta semana se diseña, implementa y documenta un **pipeline de datos completo**, siguiendo buenas prácticas de arquitectura, manejo de errores y preparación para producción.

El repositorio funciona como una **bitácora técnica**, donde el README se actualiza diariamente con el avance del proyecto.

---

## Objetivo General de la Semana
- Diseñar una arquitectura de datos alineada a requisitos de negocio
- Implementar un pipeline de datos end-to-end
- Aplicar manejo de errores y logging
- Validar y probar el pipeline
- Optimizar rendimiento y documentar el sistema

---

## 🛠️ Tecnologías utilizadas
- Python
- Pandas
- PostgreSQL
- Apache Airflow
- Linux (Ubuntu)
- Git / GitHub
- Markdown para documentación

---

## Desarrollo de la semana

### Día 1 – Diseño de Arquitectura Completa

#### Objetivo del día
Diseñar una arquitectura básica de datos para un sistema de analítica,
definiendo componentes, decisiones tecnológicas y criterios de diseño.

---

#### Actividades realizadas
- Identificación de componentes principales del sistema
- Definición del flujo de datos (ingesta → procesamiento → almacenamiento → consumo)
- Documentación de decisiones arquitectónicas

---

#### Arquitectura definida
Se definió una arquitectura simplificada orientada a analítica de retail, considerando fuentes de datos, procesamiento, almacenamiento y consumo.

---

#### Decisiones arquitectónicas
- Base de datos: PostgreSQL por su madurez y facilidad de uso
- Orquestación: Apache Airflow como estándar de la industria
- Visualización: Herramientas orientadas a negocio

---

#### Verificación – Día 1

**¿Qué factores considerarías al elegir entre una arquitectura simple vs compleja?**
- Volumen y frecuencia de datos
- Requisitos del negocio
- Presupuesto disponible
- Capacidad y experiencia del equipo
- Escalabilidad futura

**¿Cómo comunicar decisiones arquitectónicas?**
- A equipos técnicos: diagramas, flujos y justificación técnica
- A stakeholders de negocio: impacto, beneficios y riesgos

---

### Día 2 – Implementación del Pipeline End-to-End

#### Objetivo del día
Implementar un pipeline básico de datos en Python que represente un flujo de extremo a extremo, incorporando manejo explícito de errores y logging, dejando la base preparada para una futura orquestación con Airflow.

---

#### Actividades realizadas
- Uso de un entorno virtual (`venv`) para aislar dependencias
- Definición de un pipeline secuencial con pasos claros
- Implementación de manejo de errores mediante excepciones controladas
- Incorporación de logging para trazabilidad de ejecución
- Ejecución del pipeline y validación de comportamiento ante errores

El código de implementación se encuentra en:
- `src/pipeline.py`
- `src/utils.py`

---

#### Descripción del pipeline
El pipeline implementado consta de tres etapas principales:
1. Captura de datos desde una fuente simulada
2. Validación y limpieza de datos
3. Persistencia de datos procesados

Se simula un error en la etapa de validación para comprobar el correcto manejo de fallos.

---

#### Manejo de errores y logging
El pipeline:
- Detecta errores de forma explícita
- Registra eventos y excepciones en logs
- Detiene la ejecución de manera controlada ante errores críticos

Esto evita resultados incorrectos y facilita el diagnóstico.

---

#### Verificación – Día 2

**¿Qué diferencia hay entre un pipeline que falla silenciosamente y uno con buen manejo de errores?**
Un pipeline con manejo de errores:
- Detecta y registra fallos
- Facilita el mantenimiento
- Protege la calidad de los datos

Un pipeline que falla silenciosamente:
- Oculta errores
- Genera resultados incorrectos
- Dificulta la detección de problemas en producción

**¿Cómo decidir cuándo reintentar vs abortar una ejecución?**
- Reintentar ante errores transitorios (red, APIs externas)
- Abortar ante errores de validación o lógica de negocio

---

### Día 3 – Validación y Pruebas
*(Pendiente)*

#### Verificación – Día 3
*(Pendiente)*

---

### Día 4 – Optimización y Rendimiento
*(Pendiente)*

#### Verificación – Día 4
*(Pendiente)*

---

### Día 5 – Documentación y Presentación
*(Pendiente)*

#### Verificación – Día 5
*(Pendiente)*

---

## Estructura del proyecto

```text
week_3_final_project/
├── architecture
│   └── architecture_diagram.txt
├── docs
│   └── architecture_retail.md
├── notes
├── src
│   ├── pipeline.py
│   ├── utils.py
│   └── __init__.py
├── logs
│   └── pipeline.log
└── README.md
