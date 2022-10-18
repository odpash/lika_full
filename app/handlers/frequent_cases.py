from aiogram import types

from app.utils import buttons, messages
from app.main import dp


@dp.message_handler(commands=["start", "help"])
async def welcome_command(message: types.Message):
    await message.reply(
        messages.START_MESSAGE,
        reply_markup=buttons.menu,
    )
