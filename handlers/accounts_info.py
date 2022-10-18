from aiogram import types

from database.db import read_db
from app import dp
from utils import messages
from utils import buttons


@dp.message_handler(lambda m: m.text == buttons.show_all_accounts_btn.text)
async def accounts_info(message: types.Message):
    accounts_information = await read_db()
    await message.reply(
        messages.accounts_info_message(accounts_information), reply_markup=buttons.menu
    )
