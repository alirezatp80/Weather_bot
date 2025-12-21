from telethon import events
from  app import client
from app.text import welcome_text


@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond(welcome_text)
