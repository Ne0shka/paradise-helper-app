# Пример взят отсюда: https://github.com/Lonami/TelethonianBotExt/blob/master/__init__.py
import os
import asyncio
import importlib

from loguru import logger


async def init(bot):
    handlers = [
        importlib.import_module(".", f"{__name__}.{file[:-3]}")

        for file in os.listdir(os.path.dirname(__file__))

        if file.endswith(".py") and file[0].isalnum()
    ]
    to_init = (_init_handler(handler, bot) for handler in handlers)
    await asyncio.gather(*(filter(None, to_init)))


async def _init_handler(handler, bot):
    h_init = getattr(handler, "init",  None)
    if not callable(h_init):
        return
    try:
        hname = handler.__name__.split(".")[-1]
        logger.info("Загрузка модуля " + hname + "...")
        h_init = await handler.init(bot)
        logger.info("Модуль " + hname + " успешно загружен!")
    except Exception:
        logger.exception("Ошибка загрузки модуля " + handler)
    else:
        if asyncio.iscoroutine(h_init):
            await h_init
