import logging
from utils import configurar_logging

pipeline_simple = {
    "paso_1": "Capturar datos de API",
    "paso_2": "Validar y limpiar datos",
    "paso_3": "Guardar en base de datos"
}

def ejecutar_pipeline_con_errores(pipeline: dict):
    for paso, descripcion in pipeline.items():
        try:
            logging.info(f"Ejecutando {paso}: {descripcion}")

            # Simulación de ejecución
            if paso == "paso_2":
                raise ValueError("Error de validación de datos")

            logging.info(f"{paso} completado exitosamente")

        except Exception as e:
            logging.error(f"Error en {paso}: {e}", exc_info=True)
            logging.warning("Abortando ejecución del pipeline")
            break

if __name__ == "__main__":
    configurar_logging()
    ejecutar_pipeline_con_errores(pipeline_simple)
