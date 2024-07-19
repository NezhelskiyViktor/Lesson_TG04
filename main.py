import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()


# Решение задачи №1
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Нажми кнопку клавиатуры', reply_markup=kb.main)  # inline_keyboard_test)


@dp.message(F.text == "Привет")
async def test_button(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}')


@dp.message(F.text == "Пока")
async def test_button(message: Message):
    await message.answer(f'Пока, {message.from_user.first_name}')


# Решение задачи №2
@dp.message(Command('links'))
async def links(message: Message):
    await message.answer(f'Кнопки ссылок', reply_markup=kb.inline_keyboard_links)


# Решение задачи №3
@dp.message(Command('dynamic'))
async def dynamic(message: Message):
    await message.answer("Динамические кнопки", reply_markup=kb.inline_keyboard_dynamic)


@dp.callback_query(F.data == 'show_more')
async def news(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text('Динамические кнопки', reply_markup=await kb.inline_keyboard_options())


@dp.callback_query(F.data == 'option_1')
async def news(callback: CallbackQuery):
    await callback.answer("Вы выбрали Опцию 1.", show_alert=True)


@dp.callback_query(F.data == 'option_2')
async def news(callback: CallbackQuery):
    await callback.answer("Вы выбрали Опцию 2.", show_alert=True)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
