from app import client
import asyncio
from config import BOT_TOKEN


async def main():
    await client.start(bot_token=BOT_TOKEN)
    print('Client started successfully')
    await client.run_until_disconnected()

if __name__ == "__main__":
    try :
        asyncio.run(main())
    except:
        print("An error occurred while running the main function.")