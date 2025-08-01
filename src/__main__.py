import asyncio

from loguru import logger

from src.bot import app_run


if __name__ == "__main__":
    try:
        asyncio.run(app_run())
    except (KeyboardInterrupt, SystemExit):
        logger.warning("Завершение работы...")
