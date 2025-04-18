import subprocess
import asyncio
import logging
from app.loader import dp, bot
from app.handlers import main_menu, education

subprocess.run(["pip", "install", "-r", "requirements.txt"])

async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_routers(main_menu.router, education.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
