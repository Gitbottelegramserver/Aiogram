from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from app import config

bot = Bot(token=config.TOKEN, parse_mode="Markdown")
dp = Dispatcher(storage=MemoryStorage())
