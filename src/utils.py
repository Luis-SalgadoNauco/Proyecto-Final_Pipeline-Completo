import logging
from pathlib import Path

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

def calcular_total_ventas(ventas):
    """
    Calcula el total de ventas por producto.

    ventas: lista de diccionarios con claves
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
