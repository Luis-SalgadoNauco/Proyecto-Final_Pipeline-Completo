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

#### Objetivo del Día
Implementar pruebas básicas para validar la lógica del pipeline de datos, asegurando que los cálculos críticos funcionen correctamente antes de avanzar hacia etapas de optimización o despliegue.

---

#### Actividades Realizadas

#### Introducción al Testing en Pipelines de Datos
Se revisó la importancia del testing en pipelines de datos, considerando que estos procesan información crítica para el negocio. Las pruebas permiten detectar errores tempranamente y evitar regresiones cuando el código evoluciona.

Se identificaron los principales tipos de pruebas aplicables a pipelines:
- **Pruebas unitarias**
- **Pruebas de integración**
- **Validación de calidad de datos**

---

#### Implementación de Función a Testear
Se utilizó una función de negocio encargada de calcular el total de ventas por producto, considerando cantidad y precio. Esta función forma parte del módulo `utils` del proyecto y representa una lógica crítica del pipeline.

---

#### Creación de Prueba Unitaria Básica
Se creó una prueba unitaria en la carpeta `tests/`, validando:
- La correcta acumulación de ventas por producto
- El manejo de múltiples registros para un mismo producto

La prueba fue implementada sin frameworks externos, utilizando `assert`, alineado al enfoque del curso y permitiendo una validación clara y directa de la lógica.

La ejecución de la prueba fue **exitosa**, confirmando el correcto funcionamiento de la función evaluada.

---

#### Verificación – Respuestas

**¿Por qué es importante testear pipelines de datos?**

Porque los pipelines procesan datos críticos para el negocio. Un error no detectado puede propagarse hasta reportes o dashboards, generando decisiones incorrectas. El testing asegura confiabilidad y calidad en el procesamiento.


**¿Qué tipos de errores son más comunes y cómo detectarlos?**

- **Errores de lógica**: detectados mediante pruebas unitarias
- **Errores de integración**: detectados al probar componentes en conjunto
- **Errores de calidad de datos**: detectados mediante validaciones de completitud, exactitud y consistencia

---

### Día 4 – Optimización y Rendimiento

#### Objetivo del día
Identificar posibles cuellos de botella en un pipeline de datos y aplicar técnicas básicas de optimización, evaluando el impacto real mediante mediciones de rendimiento.

---

#### Actividades realizadas
- Análisis conceptual de cuellos de botella en pipelines de datos (ingesta, procesamiento, almacenamiento e I/O).
- Implementación de medición de tiempo de ejecución para funciones de procesamiento.
- Comparación entre una versión secuencial y una versión alternativa de procesamiento de datos.
- Ejecución de pruebas con diferentes volúmenes de datos para evaluar impacto de la optimización.
- Generación de evidencia persistente de los resultados obtenidos.

---

#### Evaluación de rendimiento
Se evaluaron dos versiones de una función de procesamiento de datos:
- Versión secuencial (baseline).
- Versión alternativa con enfoque “optimizado”.

Las pruebas se realizaron con:
- Volumen moderado de datos.
- Volumen grande (1.000.000 de registros).

Los resultados demostraron que:
- Para ciertos escenarios, la versión alternativa no presenta mejoras significativas.
- El uso de estructuras y operaciones internas de Python puede introducir overhead adicional.
- La optimización debe basarse en métricas reales y no en supuestos teóricos.

---

#### Evidencia generada
Los resultados de las pruebas de rendimiento fueron almacenados como evidencia técnica en archivos de texto:

- `docs/performance_day4.txt`
- `docs/performance_day4_large.txt`

Estos archivos contienen:
- Cantidad de registros procesados.
- Tiempo de ejecución de cada versión.
- Comparación directa de rendimiento.
- Conclusión de la prueba.

---

#### Verificación – Respuestas

**¿Cuándo deberías optimizar el rendimiento?**  
Cuando existen cuellos de botella identificados mediante métricas reales y el impacto justifica el aumento de complejidad.

**¿Qué compensaciones considerar entre velocidad y complejidad?**  
Una optimización puede mejorar tiempos de ejecución, pero también aumentar la complejidad del código, dificultar el mantenimiento y reducir la legibilidad. Siempre se debe evaluar el balance entre rendimiento, claridad y costo operativo.

---

### Día 5 – Documentación y Presentación

#### Objetivo del día
Documentar técnicamente el pipeline desarrollado durante la semana y preparar una comunicación clara de resultados, considerando distintas audiencias (técnica y de negocio).

---

#### Documentación técnica

Se reforzó la importancia de documentar correctamente los componentes del pipeline para facilitar el mantenimiento, reducir errores y acelerar el onboarding de nuevos integrantes del equipo.

Se documentó el componente de validación de datos de ventas, incorporando:
- Propósito claro del componente
- Reglas de validación
- Estructura de salida
- Ejemplo de uso probado en entorno local

El componente `validar_datos_ventas` valida criterios básicos de calidad antes del procesamiento:
- El precio debe ser mayor a 0
- La fecha no puede estar vacía
- Se reportan errores detallados por fila

La función fue integrada y ejecutada exitosamente desde `src/utils.py`, validando su correcto funcionamiento.

---

#### Comunicación de resultados

Se trabajó en la estructuración de un **resumen ejecutivo**, orientado a audiencias no técnicas, destacando impacto, beneficios y métricas clave del proyecto.

Resumen ejecutivo del proyecto:

- **Proyecto:** Pipeline de Analytics de Ventas
- **Objetivo:** Automatizar reportes de ventas semanales
- **Solución implementada:** Pipeline ETL con validaciones de calidad de datos
- **Beneficios principales:**
  - Reducción del tiempo de reporte: 3 días → 2 horas
  - Mejora en la calidad de datos: 95% de precisión
  - Ahorro anual estimado: €50,000
- **Métricas clave:**
  - Tiempo de procesamiento: 2 horas
  - Precisión de datos: 95%
  - Disponibilidad del sistema: 99.5%

Este enfoque permite comunicar el valor del pipeline tanto a equipos técnicos como a stakeholders de negocio.

---

#### Verificación

**¿Cómo adaptar una presentación técnica para diferentes audiencias?**

- Audiencia técnica: detalles de implementación, validaciones, métricas técnicas y decisiones de diseño.
- Audiencia de negocio: impacto, beneficios, ahorro de tiempo y mejora en la toma de decisiones.
- Audiencia ejecutiva: resumen ejecutivo, resultados clave y retorno de inversión.

**¿Qué elementos son más importantes en la documentación?**

- README: visión general y guía principal del proyecto.
- Código comentado y docstrings: comprensión técnica detallada.
- Diagramas: entendimiento rápido de la arquitectura.

La combinación de estos elementos asegura una documentación clara, mantenible y profesional.

---

## Estructura del proyecto

```text
week_3_final_project/
├── architecture/
│   └── architecture_diagram.txt
├── docs/
│   ├── architecture_retail.md
│   ├── performance_day4.txt
│   └── performance_day4_large.txt
├── logs/
│   └── pipeline.log
├── notes/
├── src/
│   ├── __init__.py
│   ├── pipeline.py
│   └── utils.py
├── tests/
│   └── test_utils.py
├── requirements.txt
├── .gitignore
└── README.md

