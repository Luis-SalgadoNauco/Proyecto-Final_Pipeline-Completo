# Arquitectura de Datos – Retail Analytics

## 1. Objetivo del sistema
Diseñar una arquitectura básica de datos para un sistema de analítica de retail,
capaz de procesar ventas e inventario y generar reportes y dashboards para el negocio.

---

## 2. Componentes principales de la arquitectura

### Ingesta
- API de ventas
- Base de datos de inventario

### Procesamiento
- Limpieza de datos
- Cálculo de métricas clave (ventas totales, stock, rotación)

### Almacenamiento
- PostgreSQL para datos limpios y estructurados

### Consumo
- Dashboard de ventas
- Reportes diarios para el negocio

---

## 3. Decisiones arquitectónicas clave

- **Base de datos**: PostgreSQL  
  *Elegida por su madurez, estabilidad y facilidad de uso.*

- **Orquestación**: Airflow  
  *Estándar de industria para pipelines ETL.*

- **Visualización**: Tableau  
  *Herramienta intuitiva para usuarios de negocio.*

---

## 4. Factores para elegir arquitectura simple vs compleja

- Volumen de datos
- Frecuencia de actualización
- Cantidad de usuarios
- Presupuesto disponible
- Nivel de criticidad del sistema

Una arquitectura simple es adecuada para volúmenes bajos y necesidades claras.
Una arquitectura compleja se justifica cuando hay gran escala o tiempo real.

---

## 5. Comunicación de decisiones arquitectónicas

### Equipo técnico
- Diagramas detallados
- Flujos de datos
- Tecnologías y configuraciones

### Stakeholders de negocio
- Beneficios del sistema
- Impacto en decisiones
- Costos y tiempos
