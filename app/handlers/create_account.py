from aiogram import types
from aiogram.dispatcher import FSMContext

from app.database.db import write_to_db
from app.handlers.frequent_cases import welcome_command
from app.utils import buttons
from app.utils.states import Add
from app.main import dp


@dp.message_handler(lambda m: m.text == buttons.add_new_account_btn.text)
async def send_create_account_1(message: types.Message):
    await message.reply("Выберите сайт:", reply_markup=buttons.sites)
    await Add.site.set()


@dp.message_handler(state=Add.site)
async def send_create_account_2(message: types.Message, state: FSMContext):
    await message.reply("Введите логин:", reply_markup=buttons.none)
    async with state.proxy() as data:
        data["site"] = message.text
    await Add.next()


@dp.message_handler(state=Add.login)
async def send_create_account_3(message: types.Message, state: FSMContext):
    await message.reply("Введите пароль:", reply_markup=buttons.none)
    async with state.proxy() as data:
        data["login"] = message.text
    await Add.next()


@dp.message_handler(state=Add.password)
async def send_create_account_4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["password"] = message.text
        await write_to_db(data.as_dict())
    await state.finish()
    await message.reply(
        "Аккаунт добавлен!", parse_mode="html", reply_markup=buttons.none
    )
    await welcome_command(message)


@dp.message_handler(state=Add.no_later_than)
async def send_create_account_5(message: types.Message, state: FSMContext):
    pass


@dp.message_handler(state=Add.remove_dates)
async def send_create_account_6(message: types.Message, state: FSMContext):
    pass


@dp.message_handler(state=Add.no_less_than)
async def send_create_account_7(message: types.Message, state: FSMContext):
    pass
