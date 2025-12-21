from telethon import TelegramClient
from config import API_ID , API_HASH

client = TelegramClient(
    session='weather_bot',
    api_id=API_ID,
    api_hash=API_HASH
)

