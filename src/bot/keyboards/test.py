from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


reply = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="ReplyKeyboardMarkup"), KeyboardButton(text="ReplyKeyboardMarkup")],
    [KeyboardButton(text="ReplyKeyboardMarkup"), KeyboardButton(text="ReplyKeyboardMarkup")],
])

inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="-->", callback_data="-->")],
    [InlineKeyboardButton(text="<--", callback_data="<--")],
])

