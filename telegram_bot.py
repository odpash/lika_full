import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

import buttons
from db import write_to_db, read_db, in_db, remove_by_id


class Add(StatesGroup):
    site = State()
    login = State()
    password = State()


class Remove(StatesGroup):
    is_active = State()


API_TOKEN = "5389632951:AAE-eYPqbHMrszD9afgtaxC6b9lbpNrWaZ0"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply(
        "Привет!\nЯ бот который поможет с записью в очередь на визу.\nВыберите действие:",
        reply_markup=buttons.menu,
    )


@dp.message_handler(lambda m: m.text == buttons.show_all_accounts_btn.text)
async def send_accounts_info(message: types.Message):
    m = ''
    d = await read_db()
    for i in d:
        m += f"Id: {i['id']}\nСайт: {i['site']}\nЛогин: {i['login']}\nПароль: {i['password']}\nТекущая дата: {i['current_date']}\n\n"
    await message.reply(f"Статистика по аккаунтам:\n{m}", reply_markup=buttons.menu)


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
    await send_welcome(message)


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
    await send_welcome(message)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
