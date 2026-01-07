from aiogram import Router, F
from aiogram.types import CallbackQuery


test = Router()

@test.callback_query(F.data == '-->')
async def test_collback(callback: CallbackQuery):
    await callback.message.edit_text(
        text = "Новый текст сообщения",
        reply_markup=callback.message.reply_markup
    )
    await callback.answer()

