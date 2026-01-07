from aiogram import Router

from .handlers.commands import commands
from .handlers.get_id import router as get_id

routers = Router()

routers.include_router(commands)
routers.include_router(get_id)
