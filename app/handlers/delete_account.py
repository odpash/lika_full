from aiogram import types
from aiogram.dispatcher import FSMContext

from app.database.db import in_db, remove_by_id
from app.handlers.frequent_cases import welcome_command
from app.utils import buttons
from app.utils.states import Remove
from app.main import *


@dp.message_handler(lambda m: m.text == buttons.delete_account_btn.text)
async def send_delete_account_1(message: types.Message):
    await message.reply("Введите ID аккаунта для удаления:", reply_markup=buttons.none)
    await Remove.is_active.set()


@dp.message_handler(state=Remove.is_active)
async def send_delete_account_2(message: types.Message, state: FSMContext):
    if not await in_db(message.text):
        await message.reply("Такого аккаунта не существует!", reply_markup=buttons.none)
    else:
        await remove_by_id(message.text)
        await message.reply("Аккаунт удален!", reply_markup=buttons.none)
    await state.finish()
    await welcome_command(message)