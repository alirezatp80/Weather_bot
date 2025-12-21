from telethon import events
from  app import client
from app.text import welcome_text
from app.buttons import submit_location_inline , main_menu , change_location
from telethon.tl.custom.message import Message
from app.utils import find_name_city

@client.on(events.NewMessage(pattern='/start'))
async def start(event: Message):
    await event.respond(welcome_text , buttons=submit_location_inline())

@client.on(events.CallbackQuery(data='submit_location'))
async def submit_location(event:events.CallbackQuery.Event):
    await event.respond("لطفاً موقعیت مکانی خود را ارسال کنید.", buttons=change_location())
    
@client.on(events.NewMessage())
async def handle_location(event:Message):
    if (event.message.geo):
        lat = event.message.geo.lat
        lon = event.message.geo.long
        city_name = find_name_city(lat,lon)
        await event.respond(f"مکان شما : {city_name}")