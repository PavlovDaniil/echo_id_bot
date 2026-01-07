from aiogram import Router

from .handlers.commands import commands
from .collbacks.test import test as collbacks_test

routers = Router()

routers.include_router(commands)
routers.include_router(collbacks_test)
