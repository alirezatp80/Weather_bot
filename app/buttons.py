from telethon import Button


def main_menu():
    profile_btn = Button.text("پروفایل")
    help_btn = Button.text("راهنما")
    today_btn = Button.text("امروز")
    future_btn = Button.text('آینده')

    structur = [
        [profile_btn,today_btn],
        [help_btn,future_btn]
        
    ]
    return structur

def change_location():
    location_btn = Button.request_location('ارسال موقعیت مکانی')
    return location_btn

