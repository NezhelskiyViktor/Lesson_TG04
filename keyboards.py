from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# Для задачи №1
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Привет")],
    [KeyboardButton(text="Пока"), ]
], resize_keyboard=True)

# Для задачи №2
inline_keyboard_links = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Новости", url='https://www.1tv.ru/news/')],
    [InlineKeyboardButton(text="Музыка", url='https://zaycev.net/')],
    [InlineKeyboardButton(text="Видео", url='https://www.youtube.com/')]
])

# Для задачи №3
inline_keyboard_dynamic = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Показать больше", callback_data='show_more')]
])


async def inline_keyboard_options():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Опция 1", callback_data='option_1'))
    keyboard.add(InlineKeyboardButton(text="Опция 2", callback_data='option_2'))
    return keyboard.adjust(2).as_markup()
