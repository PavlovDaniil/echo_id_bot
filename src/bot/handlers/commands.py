from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command
from src.bot.keyboards import test

commands = Router()

@commands.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Hello!", reply_markup=test.reply)

@commands.message(Command("info"))
async def cmd_info(message: Message):
    await message.answer("info", reply_markup=test.inline)

@commands.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("help")
