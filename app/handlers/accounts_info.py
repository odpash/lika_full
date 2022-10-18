from aiogram import types

from app.database.db import read_db
from app.utils import buttons, messages
from app.main import *


@dp.message_handler(lambda m: m.text == buttons.show_all_accounts_btn.text)
async def send_accounts_info(message: types.Message):
    accounts_information = await read_db()
    await message.reply(
        messages.accounts_info_message(accounts_information), reply_markup=buttons.menu
    )
