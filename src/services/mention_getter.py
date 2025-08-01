from telethon.tl.types import MessageEntityMention, MessageEntityMentionName


async def get_mention_link(user):
    return f"<a href=\"tg://user?id={user.id}\">{user.first_name}</a>"


async def get_mentioned_user(event):
    if event.message.entities is not None:
        for e in event.message.entities:
            if type(e) == MessageEntityMention:
                username = event.message.message[e.offset:e.offset+e.length]
                return await event.client.get_entity(username)
            if type(e) == MessageEntityMentionName:
                return await event.client.get_entity(e.user_id)
    return
