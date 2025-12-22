from telethon import events , Button
from  app import client
from app.text import welcome_text , help_text
from app.buttons import submit_location_inline , main_menu , change_location
from telethon.tl.custom.message import Message
from app.utils import find_name_city
from app.database import insert_user ,update_location , select_user
from app.api_weather import today_weather

manage_state = []

@client.on(events.NewMessage(pattern='/start'))
async def start(event: Message):
   user = {
       'id': event.sender_id,
       'name': event.sender.first_name,
       'location': None
   }
   insert_user(user['id'], user['name'], user['location'])
   await event.respond(welcome_text , buttons=submit_location_inline())

@client.on(events.CallbackQuery(data='submit_location'))
async def submit_location(event:events.CallbackQuery.Event):
    await event.edit(welcome_text)
    await event.respond("لطفاً موقعیت مکانی خود را ارسال کنید.", buttons=change_location())
    manage_state.append('location_requested')
    
@client.on(events.NewMessage())
async def handle_location(event:Message):
    user_input = (event.message.text).strip()
    if (event.message.geo)and manage_state and('location_requested' == manage_state[-1]):
        try:
            lat = event.message.geo.lat
            lon = event.message.geo.long
            city_name = find_name_city(lat,lon)
            await event.delete()
            await event.respond(f"مکان شما : {city_name}",buttons=main_menu())
            location = f'{lat},{lon}'
            user ={
                'id': event.sender_id,
                'name': event.sender.first_name,
                'location': location
            }
            update_location(user['id'], user['location'])
            manage_state.pop()
        except:
            await event.delete()
            await event.respond("خطا در پیدا کردن نام شهر. لطفاً دوباره تلاش کنید.",buttons=change_location())
    if  user_input== 'موقعیت مکانی':
        manage_state.append('location_requested')
    elif user_input == 'امروز':
        manage_state.append('today')
    elif user_input == 'آینده':
        manage_state.append('future')
    elif user_input == 'راهنما':
        manage_state.append('help')
        
@client.on(events.NewMessage())
async def handle_mainmenu(event: Message):
    if manage_state and manage_state[-1] == 'location_requested':
        await event.delete()
        await event.respond("لطفاً موقعیت مکانی خود را ارسال کنید.", buttons=change_location())
    elif manage_state and manage_state[-1] == 'today':
        user = select_user(event.sender_id)
        if user and user[2] and user[2] != None:
            text = today_weather(user[2])
            await event.respond(text)
            manage_state.pop()
        else:
            await event.respond('sorry')
    elif manage_state and manage_state[-1] == 'future':
        user = select_user(event.sender_id)
        if user and user[2] and user[2] != None:
            text = today_weather(user[2], days=7)
            await event.respond(text)
            manage_state.pop()
        else:
            await event.respond('sorry')
            
    elif manage_state and manage_state[-1] == 'help':
        await event.respond(f'{help_text}')
        manage_state.pop()
    
    else :
       if manage_state:
            print('ho')
            await event.respond('خطا لطفا یک گزینه انتخاب کنید ')
        
            
        