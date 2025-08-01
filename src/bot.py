from loguru import logger
from telethon import TelegramClient

from src import handlers
from src.utils import setup_logger, load_config


async def app_run():
    setup_logger()
    logger.info("Инициализация бота...")
    config = load_config()
    bot = TelegramClient(
        "bot",
        api_id=int(config.get("API_ID", 0)),
        api_hash=config.get("API_HASH"),
    )
    try:
        await bot.start(bot_token=config.get("BOT_TOKEN"))
        await handlers.init(bot)
        logger.info("Бот {} в сети!".format((await bot.get_me()).username))
        await bot.run_until_disconnected()
    finally:
        await bot.disconnect()
