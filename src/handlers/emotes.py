from telethon import events

from src.services import emotes_helper


async def init(bot):
    @bot.on(events.NewMessage(pattern="(?i)!? ?hug"))
    @bot.on(events.NewMessage(pattern="!? ?[оО][бБ][нН][яЯ]([лЛ]|[тТ][ьЬ])"))
    async def handler(event):
        if event.is_group:
            sender, receiver = await emotes_helper.get_targets(event)
            if sender and receiver:
                await event.reply(f"{sender} обнимает {receiver}", file=await emotes_helper.get_gif("hug"), parse_mode="html")

    @bot.on(events.NewMessage(pattern="(?i)!? ?kiss"))
    @bot.on(events.NewMessage(pattern="!? ?([чЧ]|[цЦ]|[тТ][ьЬ])[мМ][оО][кК]"))
    @bot.on(events.NewMessage(pattern="!? ?[пП][оО][цЦ][еЕ][лЛ][оО][вВ][аА]([лЛ]|[тТ][ьЬ])"))
    async def handler(event):
        if event.is_group:
            sender, receiver = await emotes_helper.get_targets(event)
            if sender and receiver:
                await event.reply(f"{sender} целует {receiver}", file=await emotes_helper.get_gif("kiss"), parse_mode="html")

    @bot.on(events.NewMessage(pattern="(?i)!? ?bite"))
    @bot.on(events.NewMessage(pattern="!? ?[кК][уУ][сС][ьЬ]"))
    @bot.on(events.NewMessage(pattern="!? ?[уУ]?[кК][уУ][сС][иИ]([лЛ]|[тТ][ьЬ])"))
    async def handler(event):
        if event.is_group:
            sender, receiver = await emotes_helper.get_targets(event)
            if sender and receiver:
                await event.reply(f"{sender} кусает {receiver}", file=await emotes_helper.get_gif("bite"), parse_mode="html")
