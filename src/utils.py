import os
import sys
import logging

from loguru import logger
from dotenv import dotenv_values


def load_config():
    return {
        **dotenv_values(".env"),
        **os.environ,
    }


def setup_logger():
    logger_format = (
        "<green>{time:DD-MM-YYYY HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{line}</cyan> "
        "- <level>{message}</level>"
    )
    logging.basicConfig(level=logging.INFO, handlers=[InterceptHandler()], force=True)
    logger.remove()
    logger.add(sys.stdout, format=logger_format, colorize=True, enqueue=True)


class InterceptHandler(logging.Handler):
    @logger.catch(default=True, onerror=lambda _: sys.exit(1))
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno
        frame, depth = sys._getframe(6), 6
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1
        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())
