from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "photo")
async def photo(message: Message):
    await message.answer_photo(
        "AgACAgIAAxkBAAMIaV5WNoEyMlrHqdqbWa0r9Mc8-bAAAtsNaxsYPflKEBhnrUjMNsIBAAMCAANtAAM4BA",
        caption="Проверка file_id"
    )

@router.message(F.text)
async def get_id_user(message: Message):
    await message.answer(f"your user id: {message.from_user.id}")

@router.message(F.photo)
async def get_photo_file_id(message: Message):
    file_id = message.photo[-1].file_id
    await message.answer(f"your photo id: {file_id}")

