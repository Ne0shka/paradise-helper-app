from aiohttp import ClientSession

from src.services import mention_getter


async def get_targets(event):
    sender = await mention_getter.get_mention_link(event.sender)
    mention = await mention_getter.get_mentioned_user(event)
    if mention is not None:
        receiver = await mention_getter.get_mention_link(mention)
        return sender, receiver
    elif event.is_reply:
        receiver = await mention_getter.get_mention_link((await event.get_reply_message()).sender)
        return sender, receiver
    else:
        return None, None


async def get_gif(emote):
    async with ClientSession("https://nekos.best") as session:
        async with session.get("/api/v2/{}".format(emote)) as resp:
            return (await resp.json())["results"][0]["url"]