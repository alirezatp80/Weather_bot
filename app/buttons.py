from telethon import Button


def main_menu():
    profile_btn = Button.text("موقعیت مکانی",resize=True,single_use=True)
    help_btn = Button.text("راهنما")
    today_btn = Button.text("امروز")
    future_btn = Button.text('آینده')

    structur = [
        [profile_btn,today_btn],
        [help_btn,future_btn]
        
    ]
    return structur

def change_location():
    location_btn = Button.request_location('ارسال موقعیت مکانی' , resize=True,single_use=True)
    return location_btn

def submit_location_inline():
    location  = Button.inline('ارسال موقعیت مکانی', data='submit_location')
    return location

