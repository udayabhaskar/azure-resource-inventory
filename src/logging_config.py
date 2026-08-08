import os
import logging


def configure_logging():

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("azure_resource_inventory")

    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("logs/inventory.log")

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger