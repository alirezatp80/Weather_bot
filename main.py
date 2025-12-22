from app import client
import asyncio
from config import BOT_TOKEN
from app import handlers 
from app.handlers import Send_today


async def main():
    await client.start(bot_token=BOT_TOKEN)
    print('Client started successfully')
    await client.loop.create_task(Send_today())
    await client.run_until_disconnected()

if __name__ == "__main__":
    try :
        asyncio.run(main())
    except Exception as e:
        print(f"An error occurred while running the main function.")