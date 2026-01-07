from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

commands = Router()

@commands.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Hello!")

@commands.message(Command("info"))
async def cmd_info(message: Message):
    await message.answer("info")

@commands.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("help")
