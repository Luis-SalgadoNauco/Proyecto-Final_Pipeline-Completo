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
