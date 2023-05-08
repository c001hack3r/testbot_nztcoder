from aiogram import Bot
from aiogram.types import Message


# Ответ на команду /старт
async def get_start(message:Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'<b>Привет, {message.from_user.first_name}! Рад тебя видеть;)</b>')
    await message.answer(f'<u>Привет, {message.from_user.first_name}! Рад тебя видеть;)</u>')
    await message.reply(f'<tg-spoiler>Привет, {message.from_user.first_name}! Рад тебя видеть;)</tg-spoiler>')