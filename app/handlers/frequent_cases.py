from aiogram import types

from app.utils import buttons, messages
from app.main import dp


@dp.message_handler(commands=["start", "help"])
async def welcome_command(message: types.Message):
    await message.reply(
        messages.start_message(),
        reply_markup=buttons.menu,
    )


@dp.message_handler(content_types=["text"])
async def no_such_command(message: types.Message):
    await message.reply(text=messages.no_such_command(), reply_markup=buttons.none)
    await welcome_command(message)
