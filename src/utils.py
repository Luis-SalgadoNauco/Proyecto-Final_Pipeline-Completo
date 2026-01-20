import logging
import time
from pathlib import Path

# ======================================================
# Logging
# ======================================================

def configurar_logging(nombre_log: str = "pipeline.log"):
    """
    Configura logging para el pipeline.
    """
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    log_path = logs_dir / nombre_log

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_path),
            logging.StreamHandler()
        ]
    )


# ======================================================
# Día 3 – Función base para testing
# ======================================================

def calcular_total_ventas(ventas):
    """
    Calcula el total de ventas por producto.

    ventas: lista de diccionarios con claves:
    - producto
    - cantidad
    - precio
    """
    totales = {}

    for venta in ventas:
        producto = venta["producto"]
        cantidad = venta["cantidad"]
        precio = venta["precio"]

        totales[producto] = totales.get(producto, 0) + (cantidad * precio)

    return totales


# ======================================================
# Día 4 – Medición de performance
# ======================================================

def medir_performance(funcion, *args):
    """
    Mide el tiempo de ejecución de una función.
    Retorna el resultado y el tiempo total.
    """
    inicio = time.time()
    resultado = funcion(*args)
    fin = time.time()

    tiempo_total = fin - inicio
    logging.info(f"Tiempo de ejecución: {tiempo_total:.4f} segundos")

    return resultado, tiempo_total


# ======================================================
# Día 4 – Procesamiento de datos (lento vs optimizado)
# ======================================================

def procesar_datos_lento(datos):
    """
    Procesamiento ineficiente (loop tradicional).
    """
    resultado = []

    for fila in datos:
        fila_procesada = fila.copy()
        fila_procesada["total"] = fila["precio"] * fila["cantidad"]
        resultado.append(fila_procesada)

    return resultado


def procesar_datos_rapido(datos):
    """
    Procesamiento optimizado usando comprensión de listas.
    """
    return [
        {**fila, "total": fila["precio"] * fila["cantidad"]}
        for fila in datos
    ]

# ======================================================
# Docstring profesioal
# ======================================================

def validar_datos_ventas(datos):
    """
    Valida la calidad de los datos de ventas antes del procesamiento.

    Reglas de validación:
    - El precio debe ser mayor a 0
    - La fecha no puede estar vacía
    - Cada fila debe contener los campos requeridos

    Args:
        datos (list): Lista de diccionarios con datos de ventas.
                      Ejemplo:
                      {'precio': 100, 'fecha': '2024-01-01'}

    Returns:
        dict: Resultado de la validación con las claves:
            - valido (bool): True si no hay errores
            - errores (list): Lista de errores encontrados
            - total_filas (int): Número total de filas evaluadas
    """
    errores = []

    for i, fila in enumerate(datos):
        if fila.get('precio', 0) <= 0:
            errores.append(f"Fila {i}: precio inválido")
        if not fila.get('fecha'):
            errores.append(f"Fila {i}: fecha faltante")

    return {
        'valido': len(errores) == 0,
        'errores': errores,
        'total_filas': len(datos)
    }
