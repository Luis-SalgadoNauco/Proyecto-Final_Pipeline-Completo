# Semana 3 – Proyecto Final: Pipeline ETL Completo

## Descripción de la semana
Durante esta semana se desarrolla el proyecto final del curso de análisis de datos,
enfocado en el diseño, implementación y documentación de un pipeline ETL completo.
El objetivo es simular un escenario real de arquitectura y procesamiento de datos,
aplicando buenas prácticas profesionales.

---

## Objetivos generales de la semana
- Diseñar una arquitectura de datos alineada a un problema de negocio
- Implementar un pipeline ETL end-to-end
- Validar calidad y consistencia de los datos
- Optimizar rendimiento y estructura del pipeline
- Documentar y presentar el proyecto final

---

## 🛠️ecnologías utilizadas
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
- Definición de flujo de datos (ingesta → procesamiento → almacenamiento → consumo)
- Documentación de decisiones arquitectónicas
- Creación de diagrama conceptual
- Análisis de criterios de arquitectura simple vs compleja

---

#### Arquitectura propuesta (conceptual)

- **Ingesta**
  - API de ventas
  - Base de datos de inventario

- **Procesamiento**
  - Limpieza de datos
  - Cálculo de métricas clave

- **Almacenamiento**
  - PostgreSQL para datos limpios y estructurados

- **Consumo**
  - Dashboard de ventas
  - Reportes diarios

---

#### Decisiones arquitectónicas clave
- **Base de datos**: PostgreSQL  
  *Elegida por su madurez, estabilidad y facilidad de uso.*

- **Orquestación**: Apache Airflow  
  *Estándar de industria para pipelines ETL.*

- **Visualización**: Tableau  
  *Herramienta intuitiva orientada a usuarios de negocio.*

---

#### Verificación

**¿Qué factores considerarías al elegir entre una arquitectura simple vs compleja?**

- Volumen de datos actual y proyectado
- Frecuencia de actualización
- Cantidad de usuarios
- Presupuesto disponible
- Criticidad del sistema

Una arquitectura simple es adecuada para escenarios con bajo volumen y menor
criticidad, mientras que una arquitectura compleja se justifica cuando se requiere
escalabilidad, alta disponibilidad y procesamiento más avanzado.

---

**¿Cómo comunicarías decisiones arquitectónicas a un equipo técnico vs stakeholders de negocio?**

- **Equipo técnico**:
  - Diagramas detallados
  - Flujos de datos
  - Tecnologías y consideraciones técnicas

- **Stakeholders de negocio**:
  - Beneficios del sistema
  - Impacto en la toma de decisiones
  - Costos, tiempos y riesgos

La comunicación debe adaptarse a la audiencia, manteniendo claridad y foco en el valor.

---

### Día 2 – Implementación del Pipeline End-to-End
*(Pendiente)*

### Día 3 – Validación y Pruebas
*(Pendiente)*

### Día 4 – Optimización y Rendimiento
*(Pendiente)*

### Día 5 – Documentación y Presentación
*(Pendiente)*

---

## Estructura del proyecto

week_3_final_project
├── architecture
│ └── architecture_diagram.txt
├── docs
│ └── architecture_retail.md
├── notes
└── README.md


