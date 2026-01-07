from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from asyncio import run
from config import Config

from bot import routers

config = Config()
config.logging.setup(level=config.logging.level, logfile=config.logging.logfile)


bot = Bot(config.telegram.bot_token)
storage = MemoryStorage()
dp = Dispatcher()

# Запуск процесса поллинга новых апдейтов
async def main():
    dp.include_router(routers)

    await dp.start_polling(bot)

if __name__ == "__main__":
    run(main())