from loguru import logger
import sys

logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> | <level>{message}</level>",
    level="INFO",
)
logger.add(
    "logs/logs_{time}.log", rotation="1 week", retention="4 weeks", compression="zip"
)

__all__ = ["logger"]
